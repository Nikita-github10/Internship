# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MilkCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 349)
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setStyleSheet("background-color:rgb(255, 224, 205)")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 14, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(85, 0, 0)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 341, 251))
        self.groupBox.setStyleSheet("QGroupBox { border: 2px solid Black;};")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.LE_Code = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Code.setGeometry(QtCore.QRect(130, 10, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Code.setFont(font)
        self.LE_Code.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Code.setObjectName("LE_Code")
        self.LE_Name = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Name.setGeometry(QtCore.QRect(130, 70, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Name.setFont(font)
        self.LE_Name.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Name.setObjectName("LE_Name")
        self.LE_Address = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Address.setGeometry(QtCore.QRect(130, 100, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Address.setFont(font)
        self.LE_Address.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Address.setObjectName("LE_Address")
        self.LE_City = QtWidgets.QLineEdit(self.groupBox)
        self.LE_City.setGeometry(QtCore.QRect(130, 150, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_City.setFont(font)
        self.LE_City.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_City.setObjectName("LE_City")
        self.LE_State = QtWidgets.QLineEdit(self.groupBox)
        self.LE_State.setGeometry(QtCore.QRect(130, 180, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_State.setFont(font)
        self.LE_State.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_State.setObjectName("LE_State")
        self.LE_Balance = QtWidgets.QLineEdit(self.groupBox)
        self.LE_Balance.setGeometry(QtCore.QRect(130, 210, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Balance.setFont(font)
        self.LE_Balance.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.LE_Balance.setObjectName("LE_Balance")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 150, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.CB_Type = QtWidgets.QComboBox(self.groupBox)
        self.CB_Type.setGeometry(QtCore.QRect(130, 40, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CB_Type.setFont(font)
        self.CB_Type.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.CB_Type.setObjectName("CB_Type")
        self.CB_Type.addItem("")
        self.CB_Type.addItem("")
        self.CB_Type.addItem("")
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(10, 310, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnAdd.setFont(font)
        self.btnAdd.setStyleSheet("background-color:rgb(180, 255, 176)")
        self.btnAdd.setObjectName("btnAdd")
        self.btnModify = QtWidgets.QPushButton(Form)
        self.btnModify.setGeometry(QtCore.QRect(80, 310, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnModify.setFont(font)
        self.btnModify.setStyleSheet("background-color:rgb(180, 255, 176)")
        self.btnModify.setObjectName("btnModify")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(150, 310, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setStyleSheet("background-color:rgb(180, 255, 176)")
        self.btnSave.setObjectName("btnSave")
        self.btnDelete = QtWidgets.QPushButton(Form)
        self.btnDelete.setGeometry(QtCore.QRect(220, 310, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setStyleSheet("background-color:rgb(180, 255, 176)")
        self.btnDelete.setObjectName("btnDelete")
        self.btnExit = QtWidgets.QPushButton(Form)
        self.btnExit.setGeometry(QtCore.QRect(290, 310, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setStyleSheet("background-color:rgb(180, 255, 176)")
        self.btnExit.setObjectName("btnExit")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(370, 50, 201, 281))
        self.listWidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.listWidget.setObjectName("listWidget")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(370, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel { border: 1px solid Black;};")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.LE_Search = QtWidgets.QLineEdit(Form)
        self.LE_Search.setGeometry(QtCore.QRect(370, 30, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LE_Search.setFont(font)
        self.LE_Search.setStyleSheet("background-color:rgb(203, 204, 255)")
        self.LE_Search.setObjectName("LE_Search")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.View_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Milk Customer"))
        self.label.setText(_translate("Form", "Milk Customer"))
        self.label_2.setText(_translate("Form", "Code :"))
        self.label_3.setText(_translate("Form", "Name :"))
        self.label_4.setText(_translate("Form", "Milk Type :"))
        self.label_5.setText(_translate("Form", "Address :"))
        self.label_6.setText(_translate("Form", "Opening Balance :"))
        self.LE_Code.setPlaceholderText(_translate("Form", "Code"))
        self.LE_Name.setPlaceholderText(_translate("Form", "Name"))
        self.LE_Address.setPlaceholderText(_translate("Form", "Adress"))
        self.LE_City.setPlaceholderText(_translate("Form", "City"))
        self.LE_State.setPlaceholderText(_translate("Form", "State"))
        self.LE_Balance.setPlaceholderText(_translate("Form", "Opening Balance"))
        self.label_7.setText(_translate("Form", "City :"))
        self.label_8.setText(_translate("Form", "State :"))
        self.CB_Type.setItemText(0, _translate("Form", "Pouch Milk"))
        self.CB_Type.setItemText(1, _translate("Form", "Lose Milk"))
        self.CB_Type.setItemText(2, _translate("Form", "Tanker Milk"))
        self.btnAdd.setText(_translate("Form", "Add"))
        self.btnModify.setText(_translate("Form", "Modify"))
        self.btnSave.setText(_translate("Form", "Save"))
        self.btnDelete.setText(_translate("Form", "Delete"))
        self.btnExit.setText(_translate("Form", "Exit"))
        self.label_9.setText(_translate("Form", "Name"))
        self.LE_Search.setPlaceholderText(_translate("Form", "Search"))
        self.LE_Code.setEnabled(False)
        self.CB_Type.setEnabled(False)
        self.LE_Name.setEnabled(False)
        self.LE_Address.setEnabled(False)
        self.LE_City.setEnabled(False)
        self.LE_State.setEnabled(False)
        self.LE_Balance.setEnabled(False)
        self.LE_Search.textChanged.connect(self.filterlist)
        self.btnAdd.clicked.connect(self.add_data)
        self.btnSave.clicked.connect(self.Save_Data)
        self.btnModify.clicked.connect(self.Update_data)
        self.btnDelete.clicked.connect(self.Delete_data)
        self.listWidget.clicked.connect(self.selectionChanged)
        self.btnExit.clicked.connect(QtWidgets.qApp.quit)

    def add_data(self):
        self.CB_Type.setEnabled(True)
        self.LE_Name.setEnabled(True)
        self.LE_Name.setFocus()
        self.LE_Address.setEnabled(True)
        self.LE_City.setEnabled(True)
        self.LE_State.setEnabled(True)
        self.LE_Balance.setEnabled(True)
        lastcode = self.listWidget.count()
        code = lastcode + 1
        print(code)
        self.LE_Code.setText(str(code))

    def filterlist(self):
        self.listWidget.clear()

    def Save_Data(self):
        Code = self.LE_Code.text()
        Type=self.CB_Type.currentText()
        Name = self.LE_Name.text()
        Address = self.LE_Address.text()
        City = self.LE_City.text()
        State = self.LE_State.text()
        Balance = self.LE_Balance.text()
        conn = sqlite3.connect('D:\Internship\ERP_Info\ERP_Info.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO MilkCustomerDB (Code,Milk_Type,Name,Address,City,State,Opening_Balance) \
                                                    VALUES (?,?,?,?,?,?,?)', (Code,Type, Name, Address, City, State, Balance))

        conn.commit()
        print("Records Inserted successfully")
        conn.close()
        self.View_data()
        self.LE_Code.clear()
        self.CB_Type.clear()
        self.LE_Name.clear()
        self.LE_Address.clear()
        self.LE_City.clear()
        self.LE_State.clear()
        self.LE_Balance.clear()

    def View_data(self):
        conn = sqlite3.connect('D:\Internship\ERP_Info\ERP_Info.db')
        cur = conn.cursor()

        cur.execute('select Name from MilkCustomerDB')
        hu = cur.fetchall()
        self.listWidget.clear()
        for i in range(len(hu)):
            item = QtWidgets.QListWidgetItem(hu[i][0])
            self.listWidget.addItem(item)

        conn.commit()
        print("Records Displayed successfully")
        conn.close()

    def Update_data(self):
        self.LE_Name.setEnabled(True)
        self.LE_Name.setFocus()
        self.CB_Type.setEnabled(True)
        self.LE_Address.setEnabled(True)
        self.LE_City.setEnabled(True)
        self.LE_State.setEnabled(True)
        self.LE_Balance.setEnabled(True)
        LE_Code = self.LE_Code.text()
        LE_Name = self.LE_Name.text()
        conn = sqlite3.connect('D:\Internship\ERP_Info\ERP_Info.db')
        cur = conn.cursor()
        cur.execute("UPDATE MilkCustomerDB SET Name = ? WHERE Code = ?", (LE_Name, LE_Code))

        conn.commit()
        print("Records Modified successfully")
        conn.close()
        self.View_data()

    def Delete_data(self):
        self.LE_Code.setFocus()
        LE_Code = self.LE_Code.text()
        conn = sqlite3.connect('D:\Internship\ERP_Info\ERP_Info.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM MilkCustomerDB WHERE Code=?", (LE_Code))
        conn.commit()
        print("Records Deleted successfully")
        conn.close()
        self.View_data()
        self.LE_Code.clear()
        self.LE_Name.clear()
        self.LE_Address.clear()
        self.LE_City.clear()
        self.LE_State.clear()
        self.LE_Balance.clear()

    def selectionChanged(self):
        name = self.listWidget.currentItem()
        cname = (name.text())
        self.LE_Name.setText(name.text())
        conn = sqlite3.connect('D:\Internship\ERP_Info\ERP_Info.db')
        cur = conn.cursor()

        cur.execute("SELECT Code FROM MilkCustomerDB WHERE Name=?", (cname,))
        result = cur.fetchone()
        code = int(''.join(map(str, result)))
        self.LE_Code.setText(str(code))

        cur.execute("SELECT Milk_Type FROM MilkCustomerDB WHERE Name=?", (cname,))
        result5 = cur.fetchone()
        type = (''.join(map(str, result5)))
        iteam = (str(type))
        print(iteam)
        self.CB_Type.setCurrentText(iteam)

        cur.execute("SELECT Address FROM MilkCustomerDB WHERE Name=?", (cname,))
        result1 = cur.fetchone()
        Add = (''.join(map(str, result1)))
        self.LE_Address.setText(str(Add))

        cur.execute("SELECT City FROM MilkCustomerDB WHERE Name=?", (cname,))
        result2 = cur.fetchone()
        city = (''.join(map(str, result2)))
        self.LE_City.setText(str(city))

        cur.execute("SELECT State FROM MilkCustomerDB WHERE Name=?", (cname,))
        result3 = cur.fetchone()
        state = (''.join(map(str, result3)))
        self.LE_State.setText(str(state))

        cur.execute("SELECT Opening_Balance FROM MilkCustomerDB WHERE Name=?", (cname,))
        result4 = cur.fetchone()
        Bal = (''.join(map(str, result4)))
        self.LE_Balance.setText(str(Bal))



        conn.commit()
        # print("Code Displayed successfully")
        conn.close()
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())