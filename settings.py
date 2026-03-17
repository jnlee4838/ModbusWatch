"""
global variables

"""

running: bool = False # running flag
appstart: bool = False # initial start flag for log file creation
flag: int = 0 # send button click
req_cnt: int = 0 # how many times of requests from QTimer per scan_rate
data_cnt: int = 0 # how many times of polling in thread return back to MainWindow
host1: str = "192"
host2: str = "168"
host3: str = "0"
host4: str = "3"
port: int = 502
slave_addr: int = 1
timeout: float = 30.0
scan_rate: int = 1000
function_code: str = "Read Holding Registers (0x03)"
start_addr: int = 0
regs_num: int = 10
data_type: str = "Uint16"
byte_order: str = "Big-Endian"
scale: float = 1.0
p_timer: float = 1000.0
