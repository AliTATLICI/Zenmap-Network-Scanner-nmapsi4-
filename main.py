# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Mar 26 21:43:19 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import nmap
import socket3
import pdf_rapor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(934, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(8)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 40, 861, 581))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 110, 221, 431))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(240, 110, 581, 221))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 1, 581, 251))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Resimler/info.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_5, icon, "")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_2.setGeometry(QtCore.QRect(240, 340, 371, 192))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_3.setGeometry(QtCore.QRect(620, 340, 201, 192))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 511, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('Tarama yapılacak ağ adresini giriniz Örneğin: 192.168.1.10/20')
        self.lineEdit.setStyleSheet("color: rgb(191, 176, 176);")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 50, 511, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('-sV -T4')
        self.lineEdit_2.setStyleSheet("color: rgb(191, 176, 176);")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(550, 10, 271, 27))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('Kaydedilen Ağ Seçiniz')
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(550, 50, 271, 27))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('Tarama Türü Seçiniz')
        self.comboBox_2.addItem('Hızlı Tara')
        self.comboBox_2.addItem('Detaylı Tarama (TCP portlarıyla)')
        self.comboBox_2.addItem('Detaylı Tarama')
        self.commandLinkButton_7 = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton_7.setGeometry(QtCore.QRect(0, 0, 31, 31))
        self.commandLinkButton_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton_7.setStyleSheet("background-color: rgb(210, 206, 206);")
        self.commandLinkButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Resimler/edit-clear-locationbar-rtl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_7.setIcon(icon1)
        self.commandLinkButton_7.setObjectName("commandLinkButton_7")
        self.commandLinkButton_8 = QtWidgets.QCommandLinkButton(self.tab)
        self.commandLinkButton_8.setGeometry(QtCore.QRect(0, 40, 31, 41))
        self.commandLinkButton_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Resimler/bookmark_add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_8.setIcon(icon2)
        self.commandLinkButton_8.setObjectName("commandLinkButton_8")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Resimler/network_local.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.progressBar = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 841, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Resimler/utilities-log-viewer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Resimler/tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Resimler/viewmag+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon6, "")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(30, 0, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Resimler/scan2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon7)
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(100, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton_2.setFont(font)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Resimler/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_2.setIcon(icon8)
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(190, 0, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton_3.setFont(font)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../Resimler/saveas3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_3.setIcon(icon9)
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton_4 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setGeometry(QtCore.QRect(330, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton_4.setFont(font)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../Resimler/clear.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_4.setIcon(icon10)
        self.commandLinkButton_4.setObjectName("commandLinkButton_4")
        self.commandLinkButton_5 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_5.setGeometry(QtCore.QRect(490, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton_5.setFont(font)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../Resimler/add.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_5.setIcon(icon11)
        self.commandLinkButton_5.setObjectName("commandLinkButton_5")
        self.commandLinkButton_6 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_6.setGeometry(QtCore.QRect(640, 0, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commandLinkButton_6.setFont(font)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../Resimler/quit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton_6.setIcon(icon12)
        self.commandLinkButton_6.setObjectName("commandLinkButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 934, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.commandLinkButton.clicked.connect(self.handleButton2)
        self.commandLinkButton_2.clicked.connect(self.kaydetButon)
        #self.pushButton_2.clicked.connect(self.handleButton2)
        self.listWidget.clicked.connect(self.handlelistWidget)
        self.comboBox_2.currentTextChanged['QString'].connect(self.taramaTuru)
        self.lineEdit.selectionChanged.connect(self.handlelineEdit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        


    def handlelineEdit(self):
        self.lineEdit.clear()
        self.lineEdit.setText('tıkl')
        self.lineEdit.setStyleSheet("color: rgb(100, 100, 176);")
        

    def kaydetButon(self):
        self.listWidget.addItem("Tara Clicked")
        pdf_goruntusu=[]
        for i in range(self.listWidget.count()):
            pdf_goruntusu.append(self.listWidget.item(i).text())
        
        print(pdf_goruntusu)
        t=pdf_rapor
        t.pdfkaydedici(pdf_goruntusu)
        #gelen_ip_listesi = socket3.run(self.lineEdit.text())
        #for i in gelen_ip_listesi:
        #    self.listWidget.addItem(i)

    def taramaTuru(self):
        
        self.listWidget.addItem(str(self.comboBox_2.currentText()))
        if str(self.comboBox_2.currentText()) == 'Hızlı Tara':
            self.lineEdit_2.setText('-T4 -F')
        elif str(self.comboBox_2.currentText()) == 'Detaylı Tarama':
            self.lineEdit_2.setText('-T4 -A -v')
        elif str(self.comboBox_2.currentText()) == 'Detaylı Tarama (TCP portlarıyla)':
            self.lineEdit_2.setText('-p 1-65535 -T4 -A -v')
            

    def handlelistWidget(self):
        self.tableWidget_4.clear() 
        ip_adresi = self.listWidget.currentItem().text()
        self.tableWidget_4.setItem(1,1, QtWidgets.QTableWidgetItem(ip_adresi))

        nm = nmap.PortScanner()
        sozluk=nm.scan(self.listWidget.currentItem().text(), '22-633')
        print(nm.command_line())  
        
        print(sozluk)
        dizi=nm.csv()
        yeni=dizi.split(";")
        print(yeni)

        tik="✔"
        
        self.tableWidget_4.clear()
        self.tableWidget_4.setHorizontalHeaderLabels(['','Port','Protokol','State','Service','Version'])
        onluk=10
        self.tableWidget_4.setColumnCount(6)
        self.tableWidget_4.setRowCount(int(len(yeni)/10)-1)
        for i in range(int(len(yeni)/10)-1):	
            self.tableWidget_4.setItem(i,0, QtWidgets.QTableWidgetItem(tik))
            self.tableWidget_4.setItem(i,1, QtWidgets.QTableWidgetItem(yeni[onluk+2]))
            self.tableWidget_4.setItem(i,2, QtWidgets.QTableWidgetItem(yeni[onluk+1]))
            self.tableWidget_4.setItem(i,3, QtWidgets.QTableWidgetItem(yeni[onluk+4]))
            self.tableWidget_4.setItem(i,4, QtWidgets.QTableWidgetItem(yeni[onluk+3]))
            self.tableWidget_4.setItem(i,5, QtWidgets.QTableWidgetItem(yeni[onluk+5]+"("+yeni[onluk+6]+")"))
            onluk=onluk+10

        

    def handleButton2(self):
        self.listWidget.addItem("Tara Clicked")
        gelen_ip_listesi = socket3.run(self.lineEdit.text())
        for i in gelen_ip_listesi:
            self.listWidget.addItem(i)
        

    def handleButton(self):
        self.pushButton_2.setText("Button Clicked")
        nm = nmap.PortScanner()
        sozluk=nm.scan(self.lineEdit.text(), '22-633')
        print(nm.command_line())  
        
        print(sozluk)
        dizi=nm.csv()
        yeni=dizi.split(";")
        print(yeni)

        tik="✔"
        
        hostlar=nm.all_hosts()
        print(hostlar)

        network = self.lineEdit.text()
        self.listWidget.addItem(network)
        
        onluk=10
        for i in range(int(len(yeni)/10)-1):	
            self.tableWidget_2.setItem(i,0, QtWidgets.QTableWidgetItem(tik))
            self.tableWidget_2.setItem(i,1, QtWidgets.QTableWidgetItem(yeni[onluk+2]))
            self.tableWidget_2.setItem(i,2, QtWidgets.QTableWidgetItem(yeni[onluk+1]))
            self.tableWidget_2.setItem(i,3, QtWidgets.QTableWidgetItem(yeni[onluk+4]))
            self.tableWidget_2.setItem(i,4, QtWidgets.QTableWidgetItem(yeni[onluk+3]))
            self.tableWidget_2.setItem(i,5, QtWidgets.QTableWidgetItem(yeni[onluk+5]+"("+yeni[onluk+6]+")"))
            onluk=onluk+10

      


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Nmapsi4"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Port"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Protokol"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "State"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Service"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Version"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Tarama Detayları"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Host Detayları"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tarama"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tarama Ekranı"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tarama Ayarları"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Nse Ayarları"))
        self.commandLinkButton.setText("Tara")
        self.commandLinkButton_2.setText("Kaydet")
        self.commandLinkButton_3.setText("Farklı Kaydet")
        self.commandLinkButton_4.setText("Geçmişi Temizle")
        self.commandLinkButton_5.setText("Favorilere Ekle")
        self.commandLinkButton_6.setText("Çıkış")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('../Resimler/nmapsi4.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
