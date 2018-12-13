import Helpers as hlp
import URLCollector as ulc
from PySide2 import QtCore, QtGui, QtWidgets


class TabWindow(object):
    def initTabs(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("PST")
        self.tabWidget.addTab(self.tab, "")

        self.Partytab = QtWidgets.QWidget()
        self.Partytab.setObjectName("Party")
        self.tabWidget.addTab(self.Partytab, "")
        self.Setup_Partytab()

        self.Combattab = QtWidgets.QWidget()
        self.Combattab.setObjectName("Combat")
        self.tabWidget.addTab(self.Combattab, "")

        self.Dungeontab = QtWidgets.QWidget()
        self.Dungeontab.setObjectName("Dungeon")
        self.tabWidget.addTab(self.Dungeontab, "")

        self.Towntab = QtWidgets.QWidget()
        self.Towntab.setObjectName("Towntab")
        self.tabWidget.addTab(self.Towntab, "")

        self.AddPlayerTab = QtWidgets.QWidget()
        self.AddPlayerTab.setObjectName("Add_Player")
        self.tabWidget.addTab(self.AddPlayerTab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Partytab), _translate("MainWindow", "Party"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Combattab), _translate("MainWindow", "Combat"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dungeontab), _translate("MainWindow", "Dungeons"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Towntab), _translate("MainWindow", "Towns"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.AddPlayerTab), _translate("MainWindow", "Add Player"))

    def Setup_Partytab(self):
        self.pushButton = QtWidgets.QPushButton(self.Partytab)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 97, 34))
        self.pushButton.setObjectName("pushButton")
        hp = hlp.Helpers()
        uc = ulc.UrlCollect()
        charobs = uc.CheckCurrentUrls()

        x = 40
        y = 30
        i = 0
        for each in charobs:
            self.namelabel = QtWidgets.QLabel(each.name, self.Partytab)
            #self.namelabel.setGeometry(x, y+100, 100, 100)
            #self.Partytab.addWidget(self.namelabel, x, y-10)
            self.tableWidget = QtWidgets.QTableWidget(self.Partytab)
            self.tableWidget.setGeometry(QtCore.QRect(x, y, 256, 256))
            self.tableWidget.setObjectName("tableWidget")
            self.tableWidget.setColumnCount(1)
            self.tableWidget.setColumnWidth(0, 200)
            self.tableWidget.setRowCount(20)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.horizontalHeader().setVisible(False)
            currentRowCount = self.tableWidget.rowCount()

            newItem = QtWidgets.QTableWidgetItem(each.name)
            self.tableWidget.setItem(0, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Armor Class : %s" % each.AC))
            self.tableWidget.setItem(1, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Base Hitpoints : %s" % each.basehitpoints))
            self.tableWidget.setItem(2, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Over Ride hitpoints : %s" % each.overridehitpoints))
            self.tableWidget.setItem(3, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Strength : %s" % each.strength))
            self.tableWidget.setItem(4, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Dexterity : %s" % each.dexterity))
            self.tableWidget.setItem(5, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("constitution : %s" % each.constitution))
            self.tableWidget.setItem(6, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("intelligence : %s" % each.intelligence))
            self.tableWidget.setItem(7, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("wisdom : %s" % each.wisdom))
            self.tableWidget.setItem(8, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Charisma : %s" % each.charisma))
            self.tableWidget.setItem(9, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Proficency : %s" % each.proficency))
            self.tableWidget.setItem(10, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str("Currency cp: %s sp: %s gp: %s" % (each.cp, each.sp, each.gp)))
            self.tableWidget.setItem(11, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str(" : %s" % each.AC))
            self.tableWidget.setItem(12, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str(" : %s" % each.AC))
            self.tableWidget.setItem(13, 0, newItem)

            newItem = QtWidgets.QTableWidgetItem(str(" : %s" % each.AC))
            self.tableWidget.setItem(14, 0, newItem)

            """
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(2, item)
            """

            x = x + 300
            if i >= 2 and y <= 30:
                y = 320
                x = 40

            i = i + 1

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_app = TabWindow()
    main_app.initTabs(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
