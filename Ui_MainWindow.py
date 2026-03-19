# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 718)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(718, 718))
        font = QFont()
        font.setFamilies([u"Lucida Sans"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #3"
                        "43434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b"
                        "1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0,"
                        " x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png"
                        ");\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcon"
                        "trol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradi"
                        "ent( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical,"
                        " QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232"
                        ", stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
" "
"   margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
""
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_Address = QGroupBox(self.centralwidget)
        self.groupBox_Address.setObjectName(u"groupBox_Address")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_Address.sizePolicy().hasHeightForWidth())
        self.groupBox_Address.setSizePolicy(sizePolicy1)
        self.groupBox_Address.setMinimumSize(QSize(700, 80))
        self.groupBox_Address.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_Address)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hLayout_F_4 = QHBoxLayout()
        self.hLayout_F_4.setSpacing(2)
        self.hLayout_F_4.setObjectName(u"hLayout_F_4")
        self.hLayout_F_4.setContentsMargins(2, 2, 2, 2)
        self.label_SlaveAddr = QLabel(self.groupBox_Address)
        self.label_SlaveAddr.setObjectName(u"label_SlaveAddr")
        sizePolicy1.setHeightForWidth(self.label_SlaveAddr.sizePolicy().hasHeightForWidth())
        self.label_SlaveAddr.setSizePolicy(sizePolicy1)
        self.label_SlaveAddr.setMinimumSize(QSize(100, 21))

        self.hLayout_F_4.addWidget(self.label_SlaveAddr)

        self.spinBox_SlaveAddr = QSpinBox(self.groupBox_Address)
        self.spinBox_SlaveAddr.setObjectName(u"spinBox_SlaveAddr")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBox_SlaveAddr.sizePolicy().hasHeightForWidth())
        self.spinBox_SlaveAddr.setSizePolicy(sizePolicy2)
        self.spinBox_SlaveAddr.setMaximumSize(QSize(80, 16777215))
        self.spinBox_SlaveAddr.setMinimum(1)
        self.spinBox_SlaveAddr.setMaximum(247)
        self.spinBox_SlaveAddr.setValue(1)
        self.spinBox_SlaveAddr.setDisplayIntegerBase(10)

        self.hLayout_F_4.addWidget(self.spinBox_SlaveAddr)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F_4.addItem(self.horizontalSpacer_8)

        self.label_ScanRate = QLabel(self.groupBox_Address)
        self.label_ScanRate.setObjectName(u"label_ScanRate")
        sizePolicy1.setHeightForWidth(self.label_ScanRate.sizePolicy().hasHeightForWidth())
        self.label_ScanRate.setSizePolicy(sizePolicy1)
        self.label_ScanRate.setMinimumSize(QSize(120, 21))

        self.hLayout_F_4.addWidget(self.label_ScanRate)

        self.spinBox_ScanRate = QSpinBox(self.groupBox_Address)
        self.spinBox_ScanRate.setObjectName(u"spinBox_ScanRate")
        sizePolicy1.setHeightForWidth(self.spinBox_ScanRate.sizePolicy().hasHeightForWidth())
        self.spinBox_ScanRate.setSizePolicy(sizePolicy1)
        self.spinBox_ScanRate.setMaximumSize(QSize(100, 16777215))
        self.spinBox_ScanRate.setMaximum(65635)
        self.spinBox_ScanRate.setValue(1000)

        self.hLayout_F_4.addWidget(self.spinBox_ScanRate, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F_4.addItem(self.horizontalSpacer_15)

        self.pushButton_Send = QPushButton(self.groupBox_Address)
        self.pushButton_Send.setObjectName(u"pushButton_Send")
        sizePolicy1.setHeightForWidth(self.pushButton_Send.sizePolicy().hasHeightForWidth())
        self.pushButton_Send.setSizePolicy(sizePolicy1)
        self.pushButton_Send.setMinimumSize(QSize(94, 0))

        self.hLayout_F_4.addWidget(self.pushButton_Send)


        self.horizontalLayout_3.addLayout(self.hLayout_F_4)


        self.gridLayout.addWidget(self.groupBox_Address, 2, 0, 1, 1)

        self.groupBox_Host = QGroupBox(self.centralwidget)
        self.groupBox_Host.setObjectName(u"groupBox_Host")
        sizePolicy1.setHeightForWidth(self.groupBox_Host.sizePolicy().hasHeightForWidth())
        self.groupBox_Host.setSizePolicy(sizePolicy1)
        self.groupBox_Host.setMinimumSize(QSize(700, 80))
        self.groupBox_Host.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_Host)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.hLayout_F_5 = QHBoxLayout()
        self.hLayout_F_5.setSpacing(2)
        self.hLayout_F_5.setObjectName(u"hLayout_F_5")
        self.hLayout_F_5.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.hLayout_F_5.setContentsMargins(2, 2, 2, 2)
        self.label_Host = QLabel(self.groupBox_Host)
        self.label_Host.setObjectName(u"label_Host")
        sizePolicy1.setHeightForWidth(self.label_Host.sizePolicy().hasHeightForWidth())
        self.label_Host.setSizePolicy(sizePolicy1)
        self.label_Host.setMinimumSize(QSize(0, 0))
        self.label_Host.setMaximumSize(QSize(100, 16777215))

        self.hLayout_F_5.addWidget(self.label_Host)

        self.lineEdit_Ip1 = QLineEdit(self.groupBox_Host)
        self.lineEdit_Ip1.setObjectName(u"lineEdit_Ip1")
        self.lineEdit_Ip1.setMaximumSize(QSize(40, 16777215))
        self.lineEdit_Ip1.setMaxLength(3)

        self.hLayout_F_5.addWidget(self.lineEdit_Ip1)

        self.lineEdit_Ip2 = QLineEdit(self.groupBox_Host)
        self.lineEdit_Ip2.setObjectName(u"lineEdit_Ip2")
        self.lineEdit_Ip2.setMaximumSize(QSize(40, 16777215))

        self.hLayout_F_5.addWidget(self.lineEdit_Ip2)

        self.lineEdit_Ip3 = QLineEdit(self.groupBox_Host)
        self.lineEdit_Ip3.setObjectName(u"lineEdit_Ip3")
        self.lineEdit_Ip3.setMaximumSize(QSize(40, 16777215))

        self.hLayout_F_5.addWidget(self.lineEdit_Ip3)

        self.lineEdit_Ip4 = QLineEdit(self.groupBox_Host)
        self.lineEdit_Ip4.setObjectName(u"lineEdit_Ip4")
        self.lineEdit_Ip4.setMaximumSize(QSize(40, 16777215))

        self.hLayout_F_5.addWidget(self.lineEdit_Ip4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F_5.addItem(self.horizontalSpacer_5)

        self.label_Port = QLabel(self.groupBox_Host)
        self.label_Port.setObjectName(u"label_Port")
        sizePolicy1.setHeightForWidth(self.label_Port.sizePolicy().hasHeightForWidth())
        self.label_Port.setSizePolicy(sizePolicy1)
        self.label_Port.setMinimumSize(QSize(0, 0))
        self.label_Port.setMaximumSize(QSize(100, 16777215))

        self.hLayout_F_5.addWidget(self.label_Port)

        self.spinBox_Port = QSpinBox(self.groupBox_Host)
        self.spinBox_Port.setObjectName(u"spinBox_Port")
        sizePolicy1.setHeightForWidth(self.spinBox_Port.sizePolicy().hasHeightForWidth())
        self.spinBox_Port.setSizePolicy(sizePolicy1)
        self.spinBox_Port.setMaximumSize(QSize(100, 16777215))
        self.spinBox_Port.setMinimum(1)
        self.spinBox_Port.setMaximum(65635)
        self.spinBox_Port.setValue(502)

        self.hLayout_F_5.addWidget(self.spinBox_Port, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addLayout(self.hLayout_F_5)


        self.gridLayout.addWidget(self.groupBox_Host, 1, 0, 1, 1)

        self.groupBox_Request = QGroupBox(self.centralwidget)
        self.groupBox_Request.setObjectName(u"groupBox_Request")
        sizePolicy1.setHeightForWidth(self.groupBox_Request.sizePolicy().hasHeightForWidth())
        self.groupBox_Request.setSizePolicy(sizePolicy1)
        self.groupBox_Request.setMinimumSize(QSize(700, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_Request)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.hLayout_F_2 = QHBoxLayout()
        self.hLayout_F_2.setSpacing(2)
        self.hLayout_F_2.setObjectName(u"hLayout_F_2")
        self.hLayout_F_2.setContentsMargins(2, 2, 2, 2)
        self.label_Func = QLabel(self.groupBox_Request)
        self.label_Func.setObjectName(u"label_Func")
        sizePolicy1.setHeightForWidth(self.label_Func.sizePolicy().hasHeightForWidth())
        self.label_Func.setSizePolicy(sizePolicy1)
        self.label_Func.setMinimumSize(QSize(80, 21))

        self.hLayout_F_2.addWidget(self.label_Func, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_Func = QComboBox(self.groupBox_Request)
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.addItem("")
        self.comboBox_Func.setObjectName(u"comboBox_Func")
        self.comboBox_Func.setMinimumSize(QSize(200, 0))
        self.comboBox_Func.setMaxVisibleItems(8)
        self.comboBox_Func.setMaxCount(8)

        self.hLayout_F_2.addWidget(self.comboBox_Func)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F_2.addItem(self.horizontalSpacer_11)

        self.label_StartAddr = QLabel(self.groupBox_Request)
        self.label_StartAddr.setObjectName(u"label_StartAddr")
        sizePolicy1.setHeightForWidth(self.label_StartAddr.sizePolicy().hasHeightForWidth())
        self.label_StartAddr.setSizePolicy(sizePolicy1)
        self.label_StartAddr.setMinimumSize(QSize(0, 21))
        self.label_StartAddr.setMaximumSize(QSize(80, 16777215))

        self.hLayout_F_2.addWidget(self.label_StartAddr, 0, Qt.AlignmentFlag.AlignLeft)

        self.spinBox_StartAddr = QSpinBox(self.groupBox_Request)
        self.spinBox_StartAddr.setObjectName(u"spinBox_StartAddr")
        sizePolicy1.setHeightForWidth(self.spinBox_StartAddr.sizePolicy().hasHeightForWidth())
        self.spinBox_StartAddr.setSizePolicy(sizePolicy1)
        self.spinBox_StartAddr.setMaximumSize(QSize(80, 16777215))
        self.spinBox_StartAddr.setMinimum(0)
        self.spinBox_StartAddr.setMaximum(65535)
        self.spinBox_StartAddr.setSingleStep(1)
        self.spinBox_StartAddr.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_StartAddr.setValue(0)

        self.hLayout_F_2.addWidget(self.spinBox_StartAddr, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F_2.addItem(self.horizontalSpacer_13)

        self.label_RegsNum = QLabel(self.groupBox_Request)
        self.label_RegsNum.setObjectName(u"label_RegsNum")
        sizePolicy1.setHeightForWidth(self.label_RegsNum.sizePolicy().hasHeightForWidth())
        self.label_RegsNum.setSizePolicy(sizePolicy1)
        self.label_RegsNum.setMinimumSize(QSize(0, 21))
        self.label_RegsNum.setMaximumSize(QSize(110, 16777215))

        self.hLayout_F_2.addWidget(self.label_RegsNum, 0, Qt.AlignmentFlag.AlignLeft)

        self.spinBox_RegsNum = QSpinBox(self.groupBox_Request)
        self.spinBox_RegsNum.setObjectName(u"spinBox_RegsNum")
        self.spinBox_RegsNum.setMaximumSize(QSize(80, 16777215))
        self.spinBox_RegsNum.setMinimum(1)
        self.spinBox_RegsNum.setMaximum(120)
        self.spinBox_RegsNum.setValue(10)

        self.hLayout_F_2.addWidget(self.spinBox_RegsNum, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_4.addLayout(self.hLayout_F_2)


        self.gridLayout.addWidget(self.groupBox_Request, 3, 0, 1, 1)

        self.groupBox_Menu = QGroupBox(self.centralwidget)
        self.groupBox_Menu.setObjectName(u"groupBox_Menu")
        sizePolicy1.setHeightForWidth(self.groupBox_Menu.sizePolicy().hasHeightForWidth())
        self.groupBox_Menu.setSizePolicy(sizePolicy1)
        self.groupBox_Menu.setMinimumSize(QSize(700, 80))
        self.groupBox_Menu.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.groupBox_Menu)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.hLayout_F = QHBoxLayout()
        self.hLayout_F.setSpacing(2)
        self.hLayout_F.setObjectName(u"hLayout_F")
        self.hLayout_F.setContentsMargins(2, 2, 2, 2)
        self.pushButton_Close = QPushButton(self.groupBox_Menu)
        self.pushButton_Close.setObjectName(u"pushButton_Close")
        sizePolicy1.setHeightForWidth(self.pushButton_Close.sizePolicy().hasHeightForWidth())
        self.pushButton_Close.setSizePolicy(sizePolicy1)
        self.pushButton_Close.setMinimumSize(QSize(94, 0))
        self.pushButton_Close.setMaximumSize(QSize(16777215, 16777215))

        self.hLayout_F.addWidget(self.pushButton_Close)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F.addItem(self.horizontalSpacer)

        self.pushButton_Connect = QPushButton(self.groupBox_Menu)
        self.pushButton_Connect.setObjectName(u"pushButton_Connect")
        sizePolicy1.setHeightForWidth(self.pushButton_Connect.sizePolicy().hasHeightForWidth())
        self.pushButton_Connect.setSizePolicy(sizePolicy1)
        self.pushButton_Connect.setMinimumSize(QSize(94, 0))
        self.pushButton_Connect.setMaximumSize(QSize(16777215, 16777215))

        self.hLayout_F.addWidget(self.pushButton_Connect)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F.addItem(self.horizontalSpacer_2)

        self.pushButton_Help = QPushButton(self.groupBox_Menu)
        self.pushButton_Help.setObjectName(u"pushButton_Help")
        sizePolicy1.setHeightForWidth(self.pushButton_Help.sizePolicy().hasHeightForWidth())
        self.pushButton_Help.setSizePolicy(sizePolicy1)
        self.pushButton_Help.setMinimumSize(QSize(94, 0))

        self.hLayout_F.addWidget(self.pushButton_Help)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hLayout_F.addItem(self.horizontalSpacer_3)

        self.pushButton_About = QPushButton(self.groupBox_Menu)
        self.pushButton_About.setObjectName(u"pushButton_About")
        sizePolicy1.setHeightForWidth(self.pushButton_About.sizePolicy().hasHeightForWidth())
        self.pushButton_About.setSizePolicy(sizePolicy1)
        self.pushButton_About.setMinimumSize(QSize(94, 0))

        self.hLayout_F.addWidget(self.pushButton_About, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addLayout(self.hLayout_F)


        self.gridLayout.addWidget(self.groupBox_Menu, 0, 0, 1, 1)

        self.groupBox_Data = QGroupBox(self.centralwidget)
        self.groupBox_Data.setObjectName(u"groupBox_Data")
        sizePolicy.setHeightForWidth(self.groupBox_Data.sizePolicy().hasHeightForWidth())
        self.groupBox_Data.setSizePolicy(sizePolicy)
        self.groupBox_Data.setMinimumSize(QSize(700, 0))
        self.gridLayout_3 = QGridLayout(self.groupBox_Data)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBox_datatype = QComboBox(self.groupBox_Data)
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.addItem("")
        self.comboBox_datatype.setObjectName(u"comboBox_datatype")
        self.comboBox_datatype.setMaxVisibleItems(5)
        self.comboBox_datatype.setMaxCount(5)

        self.horizontalLayout_5.addWidget(self.comboBox_datatype)

        self.comboBox_byteorder = QComboBox(self.groupBox_Data)
        self.comboBox_byteorder.addItem("")
        self.comboBox_byteorder.addItem("")
        self.comboBox_byteorder.setObjectName(u"comboBox_byteorder")

        self.horizontalLayout_5.addWidget(self.comboBox_byteorder)

        self.lineEdit_scale = QLineEdit(self.groupBox_Data)
        self.lineEdit_scale.setObjectName(u"lineEdit_scale")
        self.lineEdit_scale.setMaximumSize(QSize(240, 16777215))
        self.lineEdit_scale.setMaxLength(6)

        self.horizontalLayout_5.addWidget(self.lineEdit_scale)


        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.tableWidget = QTableWidget(self.groupBox_Data)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(2, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(3, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(4, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(5, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(6, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(7, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(8, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setItem(9, 1, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_Data, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_Func.setCurrentIndex(2)
        self.comboBox_datatype.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_Address.setTitle(QCoreApplication.translate("MainWindow", u"Slave Address && Scan Rate Settings", None))
        self.label_SlaveAddr.setText(QCoreApplication.translate("MainWindow", u"Slave Address", None))
        self.label_ScanRate.setText(QCoreApplication.translate("MainWindow", u"Scan Rate (ms)", None))
        self.pushButton_Send.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.groupBox_Host.setTitle(QCoreApplication.translate("MainWindow", u"Slave IP && Port Settings", None))
        self.label_Host.setText(QCoreApplication.translate("MainWindow", u"Slave IP", None))
        self.lineEdit_Ip1.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.lineEdit_Ip1.setText(QCoreApplication.translate("MainWindow", u"192", None))
        self.lineEdit_Ip2.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.lineEdit_Ip2.setText(QCoreApplication.translate("MainWindow", u"168", None))
        self.lineEdit_Ip3.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.lineEdit_Ip3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_Ip4.setInputMask(QCoreApplication.translate("MainWindow", u"000", None))
        self.lineEdit_Ip4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_Port.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.groupBox_Request.setTitle(QCoreApplication.translate("MainWindow", u"Modbus Request Settings", None))
        self.label_Func.setText(QCoreApplication.translate("MainWindow", u"Func Code", None))
        self.comboBox_Func.setItemText(0, QCoreApplication.translate("MainWindow", u"Read Coils (0x01)", None))
        self.comboBox_Func.setItemText(1, QCoreApplication.translate("MainWindow", u"Read Discrete Inputs (0x02)", None))
        self.comboBox_Func.setItemText(2, QCoreApplication.translate("MainWindow", u"Read Holding Registers (0x03)", None))
        self.comboBox_Func.setItemText(3, QCoreApplication.translate("MainWindow", u"Read Input Registers (0x04)", None))
        self.comboBox_Func.setItemText(4, QCoreApplication.translate("MainWindow", u"Write Single Coil (0x05)", None))
        self.comboBox_Func.setItemText(5, QCoreApplication.translate("MainWindow", u"Write Single Register (0x06)", None))
        self.comboBox_Func.setItemText(6, QCoreApplication.translate("MainWindow", u"Write Multiple Coils (0x0F)", None))
        self.comboBox_Func.setItemText(7, QCoreApplication.translate("MainWindow", u"Write Multiple Registers (0x10)", None))

        self.label_StartAddr.setText(QCoreApplication.translate("MainWindow", u"Start Address", None))
        self.label_RegsNum.setText(QCoreApplication.translate("MainWindow", u"Number of Regs", None))
        self.groupBox_Menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton_Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_Connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_Help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.pushButton_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.groupBox_Data.setTitle(QCoreApplication.translate("MainWindow", u"Data", None))
        self.comboBox_datatype.setItemText(0, QCoreApplication.translate("MainWindow", u"Int16", None))
        self.comboBox_datatype.setItemText(1, QCoreApplication.translate("MainWindow", u"Uint16", None))
        self.comboBox_datatype.setItemText(2, QCoreApplication.translate("MainWindow", u"Int32", None))
        self.comboBox_datatype.setItemText(3, QCoreApplication.translate("MainWindow", u"Uint32", None))
        self.comboBox_datatype.setItemText(4, QCoreApplication.translate("MainWindow", u"Float32", None))

        self.comboBox_datatype.setCurrentText(QCoreApplication.translate("MainWindow", u"Uint16", None))
        self.comboBox_byteorder.setItemText(0, QCoreApplication.translate("MainWindow", u"Big-Endian", None))
        self.comboBox_byteorder.setItemText(1, QCoreApplication.translate("MainWindow", u"Little-Endian", None))

        self.lineEdit_scale.setText(QCoreApplication.translate("MainWindow", u"1", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

