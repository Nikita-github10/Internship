# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Transporter_Info.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 300)
        Form.setMaximumSize(QtCore.QSize(600, 300))
        Form.setStyleSheet("background-color: rgb(135, 189, 216);\n"
"background-color: rgb(225, 114, 255);\n"
"background-color: rgb(255, 211, 196);")
        self.code_lbl = QtWidgets.QLabel(Form)
        self.code_lbl.setGeometry(QtCore.QRect(30, 60, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.code_lbl.setFont(font)
        self.code_lbl.setObjectName("code_lbl")
        self.Transporter_name_lbl = QtWidgets.QLabel(Form)
        self.Transporter_name_lbl.setGeometry(QtCore.QRect(30, 90, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Transporter_name_lbl.setFont(font)
        self.Transporter_name_lbl.setObjectName("Transporter_name_lbl")
        self.Address_lbl = QtWidgets.QLabel(Form)
        self.Address_lbl.setGeometry(QtCore.QRect(30, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Address_lbl.setFont(font)
        self.Address_lbl.setObjectName("Address_lbl")
        self.City_lbl = QtWidgets.QLabel(Form)
        self.City_lbl.setGeometry(QtCore.QRect(30, 150, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.City_lbl.setFont(font)
        self.City_lbl.setObjectName("City_lbl")
        self.Phone_lbl = QtWidgets.QLabel(Form)
        self.Phone_lbl.setGeometry(QtCore.QRect(30, 180, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Phone_lbl.setFont(font)
        self.Phone_lbl.setObjectName("Phone_lbl")
        self.code_txt = QtWidgets.QLineEdit(Form)
        self.code_txt.setGeometry(QtCore.QRect(160, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.code_txt.setFont(font)
        self.code_txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.code_txt.setObjectName("code_txt")
        self.Transporter_name_txt = QtWidgets.QLineEdit(Form)
        self.Transporter_name_txt.setGeometry(QtCore.QRect(160, 90, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Transporter_name_txt.setFont(font)
        self.Transporter_name_txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Transporter_name_txt.setObjectName("Transporter_name_txt")
        self.Address_txt = QtWidgets.QLineEdit(Form)
        self.Address_txt.setGeometry(QtCore.QRect(160, 120, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Address_txt.setFont(font)
        self.Address_txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Address_txt.setObjectName("Address_txt")
        self.City_txt = QtWidgets.QLineEdit(Form)
        self.City_txt.setGeometry(QtCore.QRect(160, 150, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.City_txt.setFont(font)
        self.City_txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.City_txt.setObjectName("City_txt")
        self.Phone_txt = QtWidgets.QLineEdit(Form)
        self.Phone_txt.setGeometry(QtCore.QRect(160, 180, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Phone_txt.setFont(font)
        self.Phone_txt.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.Phone_txt.setObjectName("Phone_txt")
        self.listWidget_name = QtWidgets.QListWidget(Form)
        self.listWidget_name.setGeometry(QtCore.QRect(390, 30, 151, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget_name.setFont(font)
        self.listWidget_name.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.listWidget_name.setObjectName("listWidget_name")
        self.Search_text = QtWidgets.QLineEdit(Form)
        self.Search_text.setGeometry(QtCore.QRect(390, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Search_text.setFont(font)
        self.Search_text.setStyleSheet("background-color: rgb(184, 212, 255);")
        self.Search_text.setObjectName("Search_text")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(160, 240, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setStyleSheet("background-color: rgb(169, 255, 198);")
        self.btnSave.setObjectName("btnSave")
        self.btnExit = QtWidgets.QPushButton(Form)
        self.btnExit.setGeometry(QtCore.QRect(310, 240, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color: rgb(169, 255, 198);")
        self.btnExit.setObjectName("btnExit")
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(230, 240, 61, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setStyleSheet("background-color: rgb(169, 255, 198);")
        self.btnDelete.setObjectName("btnDelete")
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(20, 240, 59, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("background-color: rgb(169, 255, 198);")
        self.btnAdd.setObjectName("btnAdd")
        self.Transporter_info_lbl = QtWidgets.QLabel(Form)
        self.Transporter_info_lbl.setGeometry(QtCore.QRect(80, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Transporter_info_lbl.setFont(font)
        self.Transporter_info_lbl.setObjectName("Transporter_info_lbl")
        self.btnModify = QtWidgets.QPushButton(Form)
        self.btnModify.setGeometry(QtCore.QRect(90, 240, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModify.setFont(font)
        self.btnModify.setStyleSheet("background-color: rgb(169, 255, 198);")
        self.btnModify.setObjectName("btnModify")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.View_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Transporter Info"))
        self.code_lbl.setText(_translate("Form", "Code"))
        self.Transporter_name_lbl.setText(_translate("Form", "Transporter Name"))
        self.Address_lbl.setText(_translate("Form", "Address"))
        self.City_lbl.setText(_translate("Form", "City"))
        self.Phone_lbl.setText(_translate("Form", "Phone"))
        self.code_txt.setText(_translate("Form", "New"))
        self.Search_text.setPlaceholderText(_translate("Form", "Search"))
        self.btnSave.setText(_translate("Form", "Save"))
        self.btnExit.setText(_translate("Form", "Exit"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnAdd.setText(_translate("Form", "Add"))
        self.Transporter_info_lbl.setText(_translate("Form", "Transporter Info"))
        self.btnModify.setText(_translate("Form", "Modify"))

        self.btnAdd.clicked.connect(self.add_data)
        self.btnSave.clicked.connect(self.save_data)
        self.btnDelete.clicked.connect(self.Delete_data)
        self.btnModify.clicked.connect(self.Update_data)
        self.listWidget_name.clicked.connect(self.selectionChanged)
        self.btnExit.clicked.connect(QtWidgets.qApp.quit)

    def selectionChanged(self):
        self.Transporter_name_txt.setEnabled(False)
        name = self.listWidget_name.currentItem()
        cname = (name.text())
        self.Transporter_name_txt.setText(name.text())
        conn = sqlite3.connect('C:\Transport\TransportDB.db')
        cur = conn.cursor()
        cur.execute("SELECT Code FROM Transport WHERE TransporterName=?", (cname,))
        result = cur.fetchone()
        # print(result)
        # print(type(result))
        res = int(''.join(map(str, result)))
        self.code_txt.setText(str(res))
        conn.commit()
        # print("Code Displayed successfully")
        conn.close()

    def filterlist(self):
        self.listWidget_name.clear()

    def add_data(self):
        self.Transporter_name_txt.setEnabled(True)
        self.Transporter_name_txt.setFocus()
        lastcode = self.listWidget_name.count()
        code = lastcode + 1
        print(code)
        self.code_txt.setText(str(code))

    def save_data(self):
        Code = self.code_txt.text()
        TName = self.Transporter_name_txt.text()
        Address=self.Address_txt.text()
        City=self.City_txt.text()
        Phone=self.Phone_txt.text()
        if Code == '' and TName == '' and Address=='' and City=='' and Phone=='':
            # Create the dialog without running it yet
            msgBox = QMessageBox()

            msgBox.setWindowTitle("Information")
            msgBox.setText(
                "No entry '" + str(Code) + " " + str(TName) + " "+str(Address)+" "+str(City)+" "+str(Phone)+"'.Would you like to add it to the database")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDefaultButton(QMessageBox.No)

            # Run the dialog, and check results
            bttn = msgBox.exec_()
            if bttn == QMessageBox.Yes:
                return True
            else:
                return False
        else:
            conn = sqlite3.connect('C:\Transport\TransportDB.db')
            cur = conn.cursor()
            cur.execute('INSERT INTO Transport (Code,TransporterName,Address,City,Phone) \
                                   VALUES (?,?,?,?,?)', (Code, TName,Address,City,Phone))

            conn.commit()
            print("Records created successfully")
            conn.close()
            self.View_data()
            self.code_txt.clear()
            self.Transporter_name_txt.clear()
            self.City_txt.clear()
            self.Address_txt.clear()
            self.Phone_txt.clear()

    def View_data(self):
        conn = sqlite3.connect('C:\Transport\TransportDB.db')
        cur = conn.cursor()
        cur.execute('select TransporterName from Transport')
        hu = cur.fetchall()
        self.listWidget_name.clear()
        for i in range(len(hu)):
                item = QtWidgets.QListWidgetItem(hu[i][0])
                self.listWidget_name.addItem(item)
        conn.commit()
        print("Records created successfully")
        conn.close()


    def Update_data(self):
        self.Transporter_name_txt.setEnabled(True)
        Code = self.code_txt.text()
        TName = self.Transporter_name_txt.text()
        conn = sqlite3.connect('C:\Transport\TransportDB.db')
        cur = conn.cursor()
        cur.execute("UPDATE Transport SET TransporterName = ? WHERE Code = ?", (TName, Code))
        conn.commit()
        print("Records Modify successfully")
        conn.close()
        self.View_data()

    def Delete_data(self):
        TName = self.Transporter_name_txt.text()
        conn = sqlite3.connect('C:\Transport\TransportDB.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM Transport WHERE TransporterName= ? ",(TName,))
        conn.commit()
        print("Records Deleted successfully")
        conn.close()
        self.View_data()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())