
import os
import sys

from datetime import *
from pyModbusTCP.client import ModbusClient
import struct

from PySide6.QtCore import (Signal, QThread, QTimer, QMutex, QMutexLocker)
from PySide6.QtWidgets import (QApplication, QDialog, QMainWindow, QTableWidgetItem)
from PySide6.QtGui import (Qt, QIcon)

import settings
from Ui_MainWindow import Ui_MainWindow

from help import Ui_Dialog as Help_Dialog
from about import Ui_Dialog as About_Dialog

basedir = os.path.join(os.path.dirname(__file__), u"RST-R-96x96.ico")

try:
    from ctypes import windll

    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass

VERSION = "0.1"

# set global
regs: list = []
# init a thread lock
regs_lock: QMutex = QMutex()


# Thread to handle incoming & outgoing TCP data
class Worker(QThread):
    # signals to send MainWindow
    error_signal = Signal(str, bool)
    data_signal = Signal(list, int)

    def __init__(self):
        super().__init__()
        self.mbm = None
        self.ip = None
        self.port = None
        self.slave_addr = None
        self.timeout = None
        self.scan_rate = None

    def request_handler(self, flag, req_cnt):
        if settings.running:
            settings.flag = flag
            settings.req_cnt = req_cnt

    # from send button or timer generation of predefined scan_rate
    def run(self):

        """Modbus polling thread."""
        global regs, regs_lock
        reg_list = None

        try:
            self.ip: str = settings.host1 + '.' + settings.host2 + '.' + settings.host3 + '.' + settings.host4
            self.port: int = settings.port
            self.slave_addr: int = settings.slave_addr
            self.timeout: float = settings.timeout
            self.scan_rate: int = settings.scan_rate

            self.mbm = ModbusClient(self.ip, self.port, self.slave_addr, self.timeout, False, False)
            self.mbm.open()

            if self.mbm.is_open:
                settings.running = True
                print(f"Thread settings.running: {settings.running}")
                settings.data_cnt = 0
                status = f"Connected"
                self.error_signal.emit(status, settings.running)
            else:
                settings.running = False
                status = f"Cannot connect"
                self.error_signal.emit(status, settings.running)

        except Exception as e:
            settings.running = False
            # exception
            print(f"Status: {e}, {type(e)}")
            status = f"{e}, {type(e)}"
            self.error_signal.emit(status, settings.running)

        while settings.running:
            if settings.flag:
                settings.flag -= 1

                # req sequence
                match settings.function_code:
                    case "Read Coils (0x01)":
                        reg_list = self.mbm.read_coils(bit_addr=settings.start_addr, bit_nb=settings.regs_num)
                        if reg_list is None:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Read Holding Registers (0x03)":
                        reg_list = self.mbm.read_holding_registers(reg_addr=settings.start_addr, reg_nb=settings.regs_num)
                        if reg_list is None:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Read Discrete Inputs (0x02)":
                        reg_list = self.mbm.read_discrete_inputs(bit_addr=settings.start_addr, bit_nb=settings.regs_num)
                        if reg_list is None:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Read Input Registers (0x04)":
                        reg_list = self.mbm.read_input_registers(reg_addr=settings.start_addr, reg_nb=settings.regs_num)
                        if reg_list is None:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Write Single Coil (0x05)":
                        ret = self.mbm.write_single_coil(bit_addr=settings.start_addr, bit_value=regs[0])
                        if ret:
                            reg_list = self.mbm.read_coils(bit_addr=settings.start_addr, bit_nb=settings.regs_num)
                        else:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Write Single Register (0x06)":
                        ret = self.mbm.write_single_register(reg_addr=settings.start_addr, reg_value=regs[0])
                        if ret:
                            reg_list = self.mbm.read_holding_registers(reg_addr=settings.start_addr, reg_nb=settings.regs_num)
                        else:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Write Multiple Coils (0x0F)":
                        ret = self.mbm.write_multiple_coils(bits_addr=settings.start_addr, bits_value=regs)
                        if ret:
                            reg_list = self.mbm.read_coils(bit_addr=settings.start_addr, bit_nb=settings.regs_num)
                        else:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)
                    case "Write Multiple Registers (0x10)":
                        ret = self.mbm.write_multiple_registers(regs_addr=settings.start_addr, regs_value=regs)
                        if ret:
                            reg_list = self.mbm.read_holding_registers(reg_addr=settings.start_addr, reg_nb=settings.regs_num)
                        else:
                            status = f"No response or invalid response"
                            self.error_signal.emit(status, settings.running)

                # recv sequence
                settings.req_cnt += 1
                print(f"Thread reg_list: {reg_list}")
                try:
                    if reg_list:
                        with QMutexLocker(regs_lock):
                            regs = list(reg_list)
                            settings.data_cnt += 1
                            self.data_signal.emit(regs, settings.data_cnt)
                    else:
                        status = f'Data {reg_list}'
                        self.error_signal.emit(status, settings.running)

                except Exception as e:
                    # settings.running = False # no need to stop thread for data error, just report error and keep going
                    # exception
                    print(f"Status: {e}, {type(e)}")
                    status = f'{e}, {type(e)}'
                    self.error_signal.emit(status, settings.running)

            # take a rest
            QThread.msleep(25)


# Help Window
class HelpWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.dialog = Help_Dialog()
        self.dialog.setupUi(self)


# Help Window
class AboutWindow(QDialog):

    def __init__(self):
        super().__init__()
        self.dialog = About_Dialog()
        self.dialog.setupUi(self)


# Main widget
class MainWindow(QMainWindow):
    # timer or manual send signal to thread
    request_signal = Signal(int, int)

    def __init__(self):
        super().__init__()

        # struct format mapping
        self.type_map = {
            "Int16": (1, 'h'),  # 1 register, signed short
            "Uint16": (1, 'H'),  # 1 register, unsigned short
            "Int32": (2, 'i'),  # 2 register, signed int
            "Uint32": (2, 'I'),  # 2 register, unsigned int
            "Float32": (2, 'f'),  # 2 register, float
        }
        self.endian_map = {
            "Big-Endian": ">",
            "Little-Endian": "<"
        }

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not os.path.isdir('log'):
            os.mkdir('log')
        self.file = None
        self.dlg_help = None
        self.dlg_about = None
        self.req_tmr = None
        self.req_num = 0  # req no.
        self.recv_num = 0  # recv no.
        # bring the default params from settings
        self.host = settings.host1 + '.' + settings.host2 + '.' + settings.host3 + '.' + settings.host4
        self.port = settings.port
        self.slave_addr = settings.slave_addr
        self.scan_rate = settings.scan_rate
        self.timeout = settings.timeout
        self.start_addr = settings.start_addr
        self.regs_num = settings.regs_num
        # QThread Creation
        self.worker_thread = Worker()
        # data to send to thread from MainWindow
        self.request_signal.connect(self.worker_thread.request_handler)
        # data to receive from thread to MainWindow
        self.worker_thread.error_signal.connect(self.error_occurred)
        self.worker_thread.data_signal.connect(self.data_handler)
        # self.worker_thread.start()
        # Polling Timer Creation
        self.p_timer = QTimer()
        self.p_timer.setInterval(self.scan_rate)
        self.p_timer.timeout.connect(self.p_timeout)
        self.p_timer_cnt = 0
        # Menu linking
        self.ui.pushButton_Close.clicked.connect(self.pushButton_close_clicked)
        self.ui.pushButton_Connect.clicked.connect(self.pushButton_connect_clicked)
        self.ui.pushButton_Help.clicked.connect(self.help_open)
        self.ui.pushButton_About.clicked.connect(self.about_open)
        # Slave IP & Port linking
        self.ui.lineEdit_Ip1.textChanged.connect(self.host_changed)
        self.ui.lineEdit_Ip2.textChanged.connect(self.host_changed)
        self.ui.lineEdit_Ip3.textChanged.connect(self.host_changed)
        self.ui.lineEdit_Ip4.textChanged.connect(self.host_changed)
        self.ui.spinBox_Port.textChanged.connect(self.host_changed)
        # Slave Address & Scan Rate linking
        self.ui.spinBox_SlaveAddr.textChanged.connect(self.slave_addr_changed)
        self.ui.spinBox_ScanRate.editingFinished.connect(self.scan_rate_changed)
        self.ui.pushButton_Send.clicked.connect(self.pushButton_send_clicked)
        # Modbus Request linking
        self.ui.comboBox_Func.currentTextChanged.connect(self.comboBox_Func_currentTextChanged)
        self.ui.spinBox_StartAddr.textChanged.connect(self.start_addr_changed)
        self.ui.spinBox_RegsNum.textChanged.connect(self.regs_number_changed)
        # Modbus Data View
        self.ui.comboBox_datatype.currentTextChanged.connect(self.datatype_changed)
        self.ui.comboBox_byteorder.currentTextChanged.connect(self.byteorder_changed)
        self.ui.lineEdit_scale.textChanged.connect(self.scale_changed)
        # Disable in case scan rate is not 0
        self.ui.pushButton_Send.setDisabled(True)
        self.setWindowTitle('ModbusWatch ' + VERSION)
        self.status = ""
        alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
        self.ui.statusbar.showMessage(alert)

    def p_timeout(self):
        if settings.running:
            self.pushButton_send_clicked()
            self.p_timer_cnt += 1
            print(f"{datetime.now().strftime("%H:%M:%S.%f")[:-3]}: {self.p_timer_cnt}")

    # first block
    def pushButton_close_clicked(self):
        win.close()

    def pushButton_connect_clicked(self, force_off=False):
        if self.ui.pushButton_Connect.text() == 'Connect' and not force_off:
            if self.host == '' or self.port == '':
                self.status = "No host assigned"
                alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
                self.ui.statusbar.showMessage(alert)
                return
            try:
                self.worker_thread.start()
                self.ui.pushButton_Connect.setText('Disconnect')
                self.setWindowTitle(self.host + ' - ' + 'ModbusWatch ' + VERSION)
                self.file = open('log/{}.log'.format(self.host.replace('/', '|')), 'a', encoding='utf-8')
                self.file.write(
                    f'\r\n========== Connect at {datetime.now().strftime("%H:%M:%S.%f")[:-3]} ==========\r\n')
                self.file.flush()
                self.status = "Trying to connect"
                alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
                self.ui.statusbar.showMessage(alert)
                settings.appstart = True
                print(f"settings.running: {settings.running}, appstart: {settings.appstart}")
                self.req_num = 0
                settings.req_cnt = self.req_num
                self.recv_num = 0
                settings.data_cnt = self.recv_num
                # Timer shot here
                if not self.p_timer.isActive() and settings.scan_rate != 0:
                    self.p_timer.start()
            except Exception as e:
                settings.running = False
                self.worker_thread.exit()
                self.status = f"{e}"
                alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
                self.ui.statusbar.showMessage(alert)

        else:  # Disconnect
            if settings.running:
                settings.running = False
                if self.worker_thread:
                    self.worker_thread.exit()
                    self.worker_thread.wait()
                    # self.worker_thread = None
            self.ui.pushButton_Connect.setText('Connect')
            self.setWindowTitle('ModbusWatch ' + VERSION)
            self.status = "Disconnected"
            alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
            self.ui.statusbar.showMessage(alert)
            try:
                if settings.appstart:
                    if self.p_timer.isActive():
                        self.p_timer.stop()
                        self.p_timer_cnt = 0
                    self.file.write(
                        f'\r\n========== Disconnect at {datetime.now().strftime("%H:%M:%S.%f")[:-3]} ==========\r\n')
                    self.file.flush()
                    if not self.file.closed:
                        QTimer.singleShot(100, self.file.close)  # wait for any pending write
            except Exception as e:
                self.status = f"{e}"
                alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
                self.ui.statusbar.showMessage(alert)
                pass

    def help_open(self):
        self.dlg_help = HelpWindow()
        self.dlg_help.show()

    def about_open(self):
        self.dlg_about = AboutWindow()
        self.dlg_about.show()

    # Second block
    def host_changed(self):
        settings.host1 = self.ui.lineEdit_Ip1.text()
        settings.host2 = self.ui.lineEdit_Ip2.text()
        settings.host3 = self.ui.lineEdit_Ip3.text()
        settings.host4 = self.ui.lineEdit_Ip4.text()
        settings.port = self.ui.spinBox_Port.value()
        self.host = settings.host1 + '.' + settings.host2 + '.' + settings.host3 + '.' + settings.host4
        self.port = settings.port
        alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
        self.ui.statusbar.showMessage(alert)
        print(f'settings.host: {self.host}:{self.port}')
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    # Third block
    def slave_addr_changed(self):
        settings.slave_addr = int(self.ui.spinBox_SlaveAddr.text())
        self.slave_addr = settings.slave_addr
        print(f'settings.slave_addr: {settings.slave_addr}')
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    def scan_rate_changed(self):
        settings.scan_rate = self.ui.spinBox_ScanRate.value()
        self.scan_rate = settings.scan_rate
        print(f'settings.scan_rate: {settings.scan_rate}')
        if settings.scan_rate == 0:
            self.ui.pushButton_Send.setEnabled(True)
        else:
            self.ui.pushButton_Send.setEnabled(False)
        if self.scan_rate != 0:
            self.p_timer.setInterval(self.scan_rate)
            self.p_timer.start()
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    def pushButton_send_clicked(self):
        print(f"req.num: {self.req_num}, settings.running: {settings.running}")
        if settings.running:
            self.req_num += 1
            if settings.data_type == "Float32" or \
                settings.data_type == "Int32" or \
                settings.data_type == "Uint32":
                is_32bit = True
            else:
                is_32bit = False
            step = 2 if is_32bit else 1

            if "Write" in settings.function_code:
                # list reset
                regs.clear()
                for i in range(0, settings.regs_num, step):
                    item = self.ui.tableWidget.item(i, 1)
                    val_str = item.text() if item else "0"
                    try:
                        if "Float" in settings.data_type:
                            val = float(val_str)
                        else:
                            val = int(float(val_str))  # exception handling "10.0"
                        fmt_type = self.type_map[settings.data_type][1]
                        fmt = self.endian_map[settings.byte_order] + fmt_type
                        packed_val = struct.pack(fmt, val)

                        # 4. hadling depending on buts (unpack & regs added)
                        if is_32bit:
                            # 32bits --> 16bits x 2 ('HH') split
                            reg1, reg2 = struct.unpack(self.endian_map[settings.byte_order] + 'HH', packed_val)
                            regs.extend([reg1, reg2])
                        else:
                            # 16bit --> 16bits x 1('H')
                            reg = struct.unpack(self.endian_map[settings.byte_order] + 'H', packed_val)[0]
                            regs.append(reg)

                    except ValueError:
                        # exception handling
                        if is_32bit:
                            regs.extend([0, 0])
                        else:
                            regs.append(0)
            print(f"pushButton_send: {regs}")
            # flag is 1 for manual send, reg values are not needed for read function but for write function, it should be sent to thread to execute write command
            self.request_signal.emit(1, self.req_num)
    
    # Fourth block
    def comboBox_Func_currentTextChanged(self):
        settings.function_code = self.ui.comboBox_Func.currentText()
        self.update_table_ui()
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    def start_addr_changed(self):
        settings.start_addr = int(self.ui.spinBox_StartAddr.text())
        self.start_addr = settings.start_addr
        self.update_table_ui()
        print(f'settings.start_addr: {settings.start_addr}')
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    def regs_number_changed(self):
        settings.regs_num = int(self.ui.spinBox_RegsNum.text())
        self.regs_num = settings.regs_num
        print(f'settings.regs_num: {settings.regs_num}')
        self.update_table_ui()
        if settings.running:
            self.pushButton_connect_clicked(force_off=True)

    def datatype_changed(self):
        settings.data_type = self.ui.comboBox_datatype.currentText()
        self.update_table_ui()
        print(f'settings.data_type: {settings.data_type}')

    def byteorder_changed(self):
        settings.byte_order = self.ui.comboBox_byteorder.currentText()
        print(f'settings.byte_order: {settings.byte_order}')

    def scale_changed(self):
        settings.scale = float(self.ui.lineEdit_scale.text())
        print(f'settings.scale: {settings.scale}')

    def update_table_ui(self):
        settings.function_code = self.ui.comboBox_Func.currentText()
        settings.regs_num = self.ui.spinBox_RegsNum.value()
        settings.start_addr = self.ui.spinBox_StartAddr.value()
        settings.data_type = self.ui.comboBox_datatype.currentText()

        self.ui.tableWidget.clearSpans()
        match settings.function_code:
            case "Read Coils (0x01)":
                settings.data_type = "Uint16"
            case "Read Holding Registers (0x03)":
                if "Float32" in settings.data_type or "Int32" in settings.data_type or "Uint32" in settings.data_type:
                    settings.regs_num = (settings.regs_num + 1) // 2 * 2  # force to add one more regs_num
            case "Read Discrete Inputs (0x02)":
                settings.data_type = "Uint16"
            case "Read Input Registers (0x04)":
                if "Float32" in settings.data_type or "Int32" in settings.data_type or "Uint32" in settings.data_type:
                    settings.regs_num = (settings.regs_num + 1) // 2 * 2  # force to add one more regs_num
            case "Write Single Coil (0x05)":
                if self.p_timer.isActive():
                    self.p_timer.stop()
                    self.p_timer_cnt = 0
                settings.scan_rate = 0
                self.scan_rate = settings.scan_rate
                print(f'settings.scan_rate: {settings.scan_rate}')
                self.ui.pushButton_Send.setEnabled(True)
                settings.regs_num = 1
                settings.data_type = "Uint16"
            case "Write Single Register (0x06)":
                if self.p_timer.isActive():
                    self.p_timer.stop()
                    self.p_timer_cnt = 0
                settings.scan_rate = 0
                self.scan_rate = settings.scan_rate
                print(f'settings.scan_rate: {settings.scan_rate}')
                self.ui.pushButton_Send.setEnabled(True)
                settings.regs_num = 1
                settings.data_type = "Uint16"
            case "Write Multiple Coils (0x0F)":
                if self.p_timer.isActive():
                    self.p_timer.stop()
                    self.p_timer_cnt = 0
                settings.scan_rate = 0
                self.scan_rate = settings.scan_rate
                print(f'settings.scan_rate: {settings.scan_rate}')
                self.ui.pushButton_Send.setEnabled(True)
                settings.data_type = "Uint16"
            case "Write Multiple Registers (0x10)":
                if self.p_timer.isActive():
                    self.p_timer.stop()
                    self.p_timer_cnt = 0
                settings.scan_rate = 0
                self.scan_rate = settings.scan_rate
                print(f'settings.scan_rate: {settings.scan_rate}')
                self.ui.pushButton_Send.setEnabled(True)
                if "Float32" in settings.data_type or "Int32" in settings.data_type or "Uint32" in settings.data_type:
                    settings.regs_num = (settings.regs_num + 1) // 2 * 2  # force to add one more regs_num
        # let's make a UI
        self.regs_num = settings.regs_num
        self.ui.spinBox_ScanRate.setValue(self.scan_rate)
        self.ui.spinBox_RegsNum.setValue(self.regs_num)
        self.ui.tableWidget.setRowCount(self.regs_num)
        self.ui.comboBox_datatype.setCurrentText(settings.data_type)
        # 32비트 데이터(Float/Int32)인 경우 2행씩 합침

        if settings.data_type == "Float32" or \
            settings.data_type == "Int32" or\
            settings.data_type ==  "Uint32":
            is_32bit = True
        else:
            is_32bit = False
        step = 2 if is_32bit else 1

        for i in range(0, settings.regs_num, step):
            # 1. add address in tableWidget
            addr_text = str(settings.start_addr + i)
            if is_32bit and (i + 1 < settings.regs_num):
                addr_text += f"---{settings.start_addr + i + 1}"
                # make cell creation
                self.ui.tableWidget.setSpan(i, 1, 2, 1) # Value
                self.ui.tableWidget.setSpan(i, 0, 2, 1) # Address

            addr_item = QTableWidgetItem(addr_text)
            addr_item.setFlags(addr_item.flags() | Qt.ItemIsUserCheckable)
            # addr_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            self.ui.tableWidget.setItem(i, 0, addr_item)

            # 2. default value
            val_item = QTableWidgetItem("0.0" if "Float32" in settings.data_type else "0")
            val_item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(i, 1, val_item)

            # make it empty to prevent an error
            if is_32bit and (i + 1 < settings.regs_num):
                self.ui.tableWidget.setItem(i + 1, 0, QTableWidgetItem(""))
                self.ui.tableWidget.setItem(i + 1, 1, QTableWidgetItem(""))

    def parse(self, reg_list, data_type, byte_order):
        step, fmt_char = self.type_map.get(data_type, (1, 'H'))
        endian = self.endian_map.get(byte_order, ">")
        parsed_results = []
        self.ui.tableWidget.setRowCount(self.regs_num)
        print(f'step: {step}, fmt_char: {fmt_char}')
        # split list per predefined step(1 or 2)
        for i in range(0, len(reg_list), step):
            block = reg_list[i: i + step]
            if len(block) < step: break  # stop if remain regs short

            # 1. convert to byte from 16 bits
            raw_bytes = struct.pack(f"{endian}{'H' * step}", *block)

            # 2. Unpack
            final_val = struct.unpack(f"{endian}{fmt_char}", raw_bytes)[0]

            # 3. apply scaling if any in Rx only case (not for Write)
            if "Registers" in settings.function_code:
                if 0 < settings.scale < 1:
                    final_val *= settings.scale
                    final_val = round(final_val, 4)
            print(f'setting.scale: {settings.scale}, final_val: {final_val}')
            # row_idx = i // step
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(str(final_val)))
            parsed_results.append(final_val)

        return parsed_results

    def data_handler(self, data, cnt):
        self.recv_num = cnt
        print(f"data_handler: {data}, {cnt}")
        data_list = self.parse(data, settings.data_type, settings.byte_order)
        c_data = f"{datetime.now().strftime('%H:%M:%S.%f')[:-3]} {self.req_num} / {self.recv_num} "
        formatted_data = ", ".join([f"{i + 1}:{val}" for i, val in enumerate(data_list)])
        c_data += f"{formatted_data}\r\n"
        self.file.write(c_data)
        self.file.flush()
        alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
        self.ui.statusbar.showMessage(alert)

    def error_occurred(self, error, flag):
        self.status = error
        alert = f"Status: {self.status} | Host: {self.host}:{self.port} | Req / Recv: {self.req_num} / {self.recv_num}"
        self.ui.statusbar.showMessage(alert)
        if not flag:
            self.ui.pushButton_Connect.setText('Connect')
            self.file = open('log/{}.log'.format(self.host.replace('/', '|')), 'a', encoding='utf-8')
            self.file.write(f'{datetime.now().strftime('%H:%M:%S.%f')[:-3]} {alert}\r\n')
            self.file.flush()

    def closeEvent(self, event):
        self.pushButton_connect_clicked(force_off=True)
        event.accept()

if __name__ == "__main__":
    # main
    app = QApplication(sys.argv)
    if os.path.isfile(basedir):
        icon = QIcon(basedir)
        app.setWindowIcon(icon)
    win = MainWindow()
    win.show()
    app.exec()

# EOF
