# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wild_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1003, 790)
        Dialog.setStyleSheet("background-color:#17212b;\n"
"color:#fff;")
        self.url_to_parse = QtWidgets.QLineEdit(Dialog)
        self.url_to_parse.setGeometry(QtCore.QRect(10, 51, 989, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.url_to_parse.setFont(font)
        self.url_to_parse.setStyleSheet("QLineEdit {\n"
"    selection-color: rgb(23, 54, 93);\n"
"border:1px solid #17365d;\n"
"padding:0 10px;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus  {\n"
"border:1px solid #17365d;\n"
"\n"
"border-radius:5px;\n"
"}")
        self.url_to_parse.setObjectName("url_to_parse")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 91, 501, 271))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"    border: 1px solid gray;\n"
"    border-color:#0e1621;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 0 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.full_name = QtWidgets.QCheckBox(self.groupBox)
        self.full_name.setGeometry(QtCore.QRect(10, 36, 271, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.full_name.setFont(font)
        self.full_name.setStyleSheet("\n"
"QCheckBox {\n"
"background-color: #0e1621;\n"
"}\n"
"\n"
"")
        self.full_name.setObjectName("full_name")
        self.brand = QtWidgets.QCheckBox(self.groupBox)
        self.brand.setGeometry(QtCore.QRect(300, 37, 181, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.brand.setFont(font)
        self.brand.setStyleSheet("background-color: #0e1621;")
        self.brand.setObjectName("brand")
        self.current_price = QtWidgets.QCheckBox(self.groupBox)
        self.current_price.setGeometry(QtCore.QRect(10, 66, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_price.setFont(font)
        self.current_price.setStyleSheet("background-color: #0e1621;")
        self.current_price.setObjectName("current_price")
        self.default_price = QtWidgets.QCheckBox(self.groupBox)
        self.default_price.setGeometry(QtCore.QRect(300, 66, 191, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.default_price.setFont(font)
        self.default_price.setStyleSheet("background-color: #0e1621;")
        self.default_price.setObjectName("default_price")
        self.url_to_product = QtWidgets.QCheckBox(self.groupBox)
        self.url_to_product.setGeometry(QtCore.QRect(9, 235, 411, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.url_to_product.setFont(font)
        self.url_to_product.setStyleSheet("background-color: #0e1621;")
        self.url_to_product.setObjectName("url_to_product")
        self.articul = QtWidgets.QCheckBox(self.groupBox)
        self.articul.setGeometry(QtCore.QRect(10, 96, 261, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.articul.setFont(font)
        self.articul.setStyleSheet("background-color: #0e1621;")
        self.articul.setObjectName("articul")
        self.rating = QtWidgets.QCheckBox(self.groupBox)
        self.rating.setGeometry(QtCore.QRect(300, 96, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rating.setFont(font)
        self.rating.setStyleSheet("background-color: #0e1621;")
        self.rating.setObjectName("rating")
        self.img_link = QtWidgets.QCheckBox(self.groupBox)
        self.img_link.setGeometry(QtCore.QRect(300, 127, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.img_link.setFont(font)
        self.img_link.setStyleSheet("background-color: #0e1621;")
        self.img_link.setObjectName("img_link")
        self.order_count = QtWidgets.QCheckBox(self.groupBox)
        self.order_count.setGeometry(QtCore.QRect(10, 156, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order_count.setFont(font)
        self.order_count.setStyleSheet("background-color: #0e1621;")
        self.order_count.setObjectName("order_count")
        self.reviews_count = QtWidgets.QCheckBox(self.groupBox)
        self.reviews_count.setGeometry(QtCore.QRect(300, 157, 191, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reviews_count.setFont(font)
        self.reviews_count.setStyleSheet("background-color: #0e1621;")
        self.reviews_count.setObjectName("reviews_count")
        self.description = QtWidgets.QCheckBox(self.groupBox)
        self.description.setGeometry(QtCore.QRect(10, 126, 261, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.description.setFont(font)
        self.description.setStyleSheet("background-color: #0e1621;")
        self.description.setObjectName("description")
        self.characteristics = QtWidgets.QCheckBox(self.groupBox)
        self.characteristics.setGeometry(QtCore.QRect(300, 184, 181, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.characteristics.setFont(font)
        self.characteristics.setStyleSheet("background-color: #0e1621;")
        self.characteristics.setObjectName("characteristics")
        self.product_quantity = QtWidgets.QCheckBox(self.groupBox)
        self.product_quantity.setGeometry(QtCore.QRect(10, 184, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.product_quantity.setFont(font)
        self.product_quantity.setStyleSheet("background-color: #0e1621;")
        self.product_quantity.setObjectName("product_quantity")
        self.sizes = QtWidgets.QCheckBox(self.groupBox)
        self.sizes.setGeometry(QtCore.QRect(10, 211, 271, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sizes.setFont(font)
        self.sizes.setStyleSheet("background-color: #0e1621;")
        self.sizes.setObjectName("sizes")
        self.colors = QtWidgets.QCheckBox(self.groupBox)
        self.colors.setGeometry(QtCore.QRect(300, 210, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.colors.setFont(font)
        self.colors.setStyleSheet("background-color: #0e1621;")
        self.colors.setObjectName("colors")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 368, 501, 101))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 0 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_2.setObjectName("groupBox_2")
        self.time_taken = QtWidgets.QLabel(self.groupBox_2)
        self.time_taken.setGeometry(QtCore.QRect(12, 50, 331, 17))
        self.time_taken.setStyleSheet("background-color: #0e1621;")
        self.time_taken.setText("")
        self.time_taken.setObjectName("time_taken")
        self.stop_parse = QtWidgets.QPushButton(self.groupBox_2)
        self.stop_parse.setGeometry(QtCore.QRect(266, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop_parse.setFont(font)
        self.stop_parse.setStyleSheet("QPushButton {\n"
"background-color: #ff5745;\n"
"border:2px solid #e32410;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 4, 14);\n"
"border:2px solid #e32410;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}")
        self.stop_parse.setObjectName("stop_parse")
        self.start_parse = QtWidgets.QPushButton(self.groupBox_2)
        self.start_parse.setGeometry(QtCore.QRect(9, 40, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_parse.setFont(font)
        self.start_parse.setStyleSheet("QPushButton {\n"
"background-color:#0b8f22;\n"
"border:2px solid #0cc42c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #0aa324;\n"
"border:2px solid rgb(0, 85, 0);\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}")
        self.start_parse.setObjectName("start_parse")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 590, 501, 191))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 0 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_3.setObjectName("groupBox_3")
        self.time_taken_2 = QtWidgets.QLabel(self.groupBox_3)
        self.time_taken_2.setGeometry(QtCore.QRect(12, 50, 331, 17))
        self.time_taken_2.setStyleSheet("background-color: #0e1621;")
        self.time_taken_2.setText("")
        self.time_taken_2.setObjectName("time_taken_2")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 70, 221, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: #0e1621;")
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(315, 70, 191, 21))
        self.label_2.setStyleSheet("background-color: #0e1621;")
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: #0e1621;")
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(316, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: #0e1621;")
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 144, 31, 31))
        self.label_11.setStyleSheet("background-color: #0e1621;")
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap(":/icon/icon.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setWordWrap(False)
        self.label_11.setObjectName("label_11")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(66, 134, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color: #0e1621;\n"
"color: rgb(10, 137, 255);")
        self.label_14.setObjectName("label_14")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(518, 91, 481, 490))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"    border: 1px solid gray;\n"
"    border-color:#0e1621;\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"}")
        self.groupBox_4.setObjectName("groupBox_4")
        self.logs_data = QtWidgets.QTextEdit(self.groupBox_4)
        self.logs_data.setGeometry(QtCore.QRect(14, 27, 456, 430))
        self.logs_data.setStyleSheet("QTextEdit {\n"
"background-color: #0e1621;\n"
"    border: 1px solid gray;\n"
"    border-color:#0e1621;\n"
"    padding-right:7px;\n"
"   \n"
"}")
        self.logs_data.setObjectName("logs_data")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(519, 590, 481, 191))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 0 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(9, 66, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: #0e1621;")
        self.label_4.setObjectName("label_4")
        self.total_product_parsed = QtWidgets.QLabel(self.groupBox_5)
        self.total_product_parsed.setGeometry(QtCore.QRect(168, 67, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_product_parsed.setFont(font)
        self.total_product_parsed.setStyleSheet("background-color: #0e1621;")
        self.total_product_parsed.setObjectName("total_product_parsed")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 38, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: #0e1621;")
        self.label_10.setObjectName("label_10")
        self.total_page_find = QtWidgets.QLabel(self.groupBox_5)
        self.total_page_find.setGeometry(QtCore.QRect(168, 38, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_page_find.setFont(font)
        self.total_page_find.setStyleSheet("background-color: #0e1621;")
        self.total_page_find.setObjectName("total_page_find")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(269, 71, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #0e1621;")
        self.label_3.setObjectName("label_3")
        self.total_prod_count = QtWidgets.QLabel(self.groupBox_5)
        self.total_prod_count.setGeometry(QtCore.QRect(284, 69, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_prod_count.setFont(font)
        self.total_prod_count.setStyleSheet("background-color: #0e1621;")
        self.total_prod_count.setText("")
        self.total_prod_count.setObjectName("total_prod_count")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(10, 139, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"background-color: #0e1621;\n"
"color: rgb(0, 170, 0);\n"
"font-size:20px;\n"
"}")
        self.label.setObjectName("label")
        self.save_parsed_data = QtWidgets.QPushButton(self.groupBox_5)
        self.save_parsed_data.setGeometry(QtCore.QRect(168, 139, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save_parsed_data.setFont(font)
        self.save_parsed_data.setStyleSheet("QPushButton {\n"
"background-color:#17212b;\n"
"border:2px solid #245dac;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #FF17365D;\n"
"\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}")
        self.save_parsed_data.setObjectName("save_parsed_data")
        self.work_text_status = QtWidgets.QLabel(self.groupBox_5)
        self.work_text_status.setGeometry(QtCore.QRect(170, 106, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.work_text_status.setFont(font)
        self.work_text_status.setStyleSheet("background-color: #0e1621;")
        self.work_text_status.setObjectName("work_text_status")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(11, 107, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: #0e1621;")
        self.label_12.setObjectName("label_12")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(6, 10, 1001, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(49, 1, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Fira Code Medium")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(10, 137, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(7, 0, 31, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/icon/icon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.close_programm = QtWidgets.QPushButton(Dialog)
        self.close_programm.setGeometry(QtCore.QRect(978, 10, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.close_programm.setFont(font)
        self.close_programm.setStyleSheet("QPushButton {\n"
"    color:#fff;\n"
"border:none;\n"
"    border-radius:15px;\n"
"\n"
"    background-color: rgb(194, 62, 64);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#fff;\n"
"border:none;\n"
"    border-radius:15px;\n"
"\n"
"    background-color:#ff1100;\n"
"\n"
"}")
        self.close_programm.setObjectName("close_programm")
        self.minimize_window = QtWidgets.QPushButton(Dialog)
        self.minimize_window.setGeometry(QtCore.QRect(949, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_window.setFont(font)
        self.minimize_window.setStyleSheet("QPushButton {\n"
"    color:#000;\n"
"    border:none;    \n"
"border-radius:15px;\n"
"    border:none;\n"
"    \n"
"    \n"
"    \n"
"    background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:#64cc14;\n"
"\n"
"}")
        self.minimize_window.setObjectName("minimize_window")
        self.groupBox_6 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 480, 501, 101))
        self.groupBox_6.setStyleSheet("QGroupBox  {\n"
"    background-color: #0e1621;\n"
"\n"
"    margin-top: 27px;\n"
"    font-size: 14px;\n"
"    border-radius: 0 5px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 5px 8000px 5px 8000px;\n"
"    background-color: #FF17365D;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.groupBox_6.setObjectName("groupBox_6")
        self.personal_key = QtWidgets.QLineEdit(self.groupBox_6)
        self.personal_key.setGeometry(QtCore.QRect(10, 60, 381, 31))
        self.personal_key.setStyleSheet("QLineEdit {\n"
"    selection-color: rgb(23, 54, 93);\n"
"border:1px solid #17365d;\n"
"padding:0 10px;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus  {\n"
"border:1px solid #17365d;\n"
"\n"
"border-radius:5px;\n"
"}")
        self.personal_key.setText("")
        self.personal_key.setObjectName("personal_key")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(10, 29, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: #0e1621;")
        self.label_13.setObjectName("label_13")
        self.activate = QtWidgets.QPushButton(self.groupBox_6)
        self.activate.setGeometry(QtCore.QRect(400, 60, 81, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.activate.setFont(font)
        self.activate.setStyleSheet("QPushButton {\n"
"background-color:#0b8f22;\n"
"border:2px solid #0cc42c;\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #0aa324;\n"
"border:2px solid rgb(0, 85, 0);\n"
"border-radius:5px;\n"
"color:#fff;\n"
"}")
        self.activate.setObjectName("activate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WildParser | Wildberries"))
        self.url_to_parse.setPlaceholderText(_translate("Dialog", "Ссылка на страницу с товарами"))
        self.groupBox.setTitle(_translate("Dialog", "Настройки парсера:"))
        self.full_name.setText(_translate("Dialog", "Полные названия"))
        self.brand.setText(_translate("Dialog", "Бренд"))
        self.current_price.setText(_translate("Dialog", "Текущая цена"))
        self.default_price.setText(_translate("Dialog", "Цена без скидки"))
        self.url_to_product.setText(_translate("Dialog", "Ссылка на страницу с товаром"))
        self.articul.setText(_translate("Dialog", "Артикул"))
        self.rating.setText(_translate("Dialog", "Рейтинг"))
        self.img_link.setText(_translate("Dialog", "Картинка товара"))
        self.order_count.setText(_translate("Dialog", "Кол-во покупок"))
        self.reviews_count.setText(_translate("Dialog", "Кол-во отзывов"))
        self.description.setText(_translate("Dialog", "Описание товара"))
        self.characteristics.setText(_translate("Dialog", "Характеристики"))
        self.product_quantity.setText(_translate("Dialog", "Остатки на складе"))
        self.sizes.setText(_translate("Dialog", "Размеры(если есть)"))
        self.colors.setText(_translate("Dialog", "Цвет"))
        self.groupBox_2.setTitle(_translate("Dialog", "Управление:"))
        self.stop_parse.setText(_translate("Dialog", "Стоп"))
        self.start_parse.setText(_translate("Dialog", "Старт"))
        self.groupBox_3.setTitle(_translate("Dialog", "О программе"))
        self.label_6.setText(_translate("Dialog", "Почта: valinorProg@gmail.com"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.donationalerts.com/r/wbpart\"><span style=\" font-size:10pt; text-decoration: underline; color:#fff;\">Поддержать проект</span></a></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://vk.com/val1n0r\"><span style=\" color:#fff;\">Автор [VK]</span></a></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><a href=\"http://valinor-dev.ru/wild-parser/\"><span style=\" color:#fff;\">Сайт программы</span></a></p></body></html>"))
        self.label_14.setText(_translate("Dialog", "WildParser | Версия 1.0"))
        self.groupBox_4.setTitle(_translate("Dialog", "Информация:"))
        self.logs_data.setPlaceholderText(_translate("Dialog", "Тут будет появляться информация о работе программы"))
        self.groupBox_5.setTitle(_translate("Dialog", "Текущая сессия:"))
        self.label_4.setText(_translate("Dialog", "Товаров получено:"))
        self.total_product_parsed.setText(_translate("Dialog", "0"))
        self.label_10.setText(_translate("Dialog", "Страниц найдено:"))
        self.total_page_find.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "/"))
        self.label.setText(_translate("Dialog", "Отчёт готов:"))
        self.save_parsed_data.setText(_translate("Dialog", "Сохранить"))
        self.work_text_status.setText(_translate("Dialog", "Ожидаем работы"))
        self.label_12.setText(_translate("Dialog", "Статус работы:"))
        self.label_8.setText(_translate("Dialog", "WildParser | Wildberries"))
        self.close_programm.setText(_translate("Dialog", "X"))
        self.minimize_window.setText(_translate("Dialog", "-"))
        self.groupBox_6.setTitle(_translate("Dialog", "Лицензия:"))
        self.personal_key.setPlaceholderText(_translate("Dialog", "Ключ активации"))
        self.label_13.setText(_translate("Dialog", "Лицензия:"))
        self.activate.setText(_translate("Dialog", "Проверить"))

