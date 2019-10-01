import Helpers as hlp
import URLCollector as ulc
import JsonHelpers as Jhel
import CharScrapper as crs
from PySide2 import QtCore, QtGui, QtWidgets


class TabWindow(object):
    def initTabs(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 900)
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
        self.Setup_Combattab()

        self.Dungeontab = QtWidgets.QWidget()
        self.Dungeontab.setObjectName("Dungeon")
        self.tabWidget.addTab(self.Dungeontab, "")

        self.Towntab = QtWidgets.QWidget()
        self.Towntab.setObjectName("Towntab")
        self.tabWidget.addTab(self.Towntab, "")

        self.AddPlayerTab = QtWidgets.QWidget()
        self.AddPlayerTab.setObjectName("Add_Player")
        self.tabWidget.addTab(self.AddPlayerTab, "")

        self.AddNoteTab = QtWidgets.QWidget()
        self.AddNoteTab.setObjectName("Add_Note")
        self.tabWidget.addTab(self.AddNoteTab, "Add Notes")
        self.Setup_Notetab()

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
            print(each, "Bandaga")
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

            newItem = QtWidgets.QTableWidgetItem(str("Current Hitpoints : %s" % (each.basehitpoints + (hp.get_mod(each.constitution) * hp.get_player_level(each.charxp)) - each.removedhp)))
            self.tableWidget.setItem(2, 0, newItem)

            #newItem = QtWidgets.QTableWidgetItem(str("Base Hitpoints : %s" % each.basehitpoints))
            #self.tableWidget.setItem(2, 0, newItem)

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

    def Setup_Combattab(self):
        #self.Comtab = QtWidgets.QPushButton(self.Combattab)
        #self.pushButton.setGeometry(QtCore.QRect(40, 30, 97, 34))
        #self.pushButton.setObjectName("pushButton")
        hp = hlp.Helpers()
        uc = ulc.UrlCollect()
        charobs = uc.CheckCurrentUrls()
        #for cbs in charobs:
        #    print(cbs, "CBS")
        #    curl = crs.CharScrape(cbs)
            #print(curl)

        x = 40
        y = 30
        i = 0
        Frame = self.Combattab
        Frame.setObjectName("Frame")
        Frame.resize(250, 141)
        self.spinBox = QtWidgets.QSpinBox(Frame)
        self.spinBox.setGeometry(QtCore.QRect(450, 30, 51, 41))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLineWidth(8)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Frame)
        self.progressBar.setGeometry(QtCore.QRect(170, 40, 311, 23))
        self.progressBar.setProperty("value", 54)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(Frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(Frame)
        self.groupBox_2.setGeometry(QtCore.QRect(90, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Frame)
        self.groupBox_3.setGeometry(QtCore.QRect(170, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(Frame)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_5 = QtWidgets.QGroupBox(Frame)
        self.groupBox_5.setGeometry(QtCore.QRect(330, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(Frame)
        self.groupBox_6.setGeometry(QtCore.QRect(410, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")

        self.groupBox_7 = QtWidgets.QGroupBox(Frame)
        self.groupBox_7.setGeometry(QtCore.QRect(490, 70, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")

        self.retranslateCombat(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateCombat(self, Frame):
        Frame.setWindowTitle(QtWidgets.QApplication.translate("Frame", "Frame", None))
        self.label.setText(QtWidgets.QApplication.translate("Frame", "Venificus", None))
        self.label_2.setText(QtWidgets.QApplication.translate("Frame", "50/54", None))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("Frame", "STR", None))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("Frame", "DEX", None))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("Frame", "CON", None))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("Frame", "INT", None))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("Frame", "WIS", None))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("Frame", "Char", None))
        self.groupBox_7.setTitle(QtWidgets.QApplication.translate("Frame", "AC", None))


    def Setup_Notetab(self):

        Frame = self.AddNoteTab
        Frame.setObjectName("Frame")
        Frame.resize(250, 141)

        font = QtGui.QFont()
        font.setPointSize(16)

        jhelp = Jhel.JsonAdd()
        jnote = Jhel.Json_Note()


        self.NoteTitleLbl = QtWidgets.QLabel("Note Name", Frame)
        self.NoteTitleLbl.setGeometry(QtCore.QRect(350, 20, 300, 61))
        self.NoteTitleLbl.setFont(font)
        self.NoteTitle = QtWidgets.QLineEdit(Frame)
        self.NoteTitle.setGeometry(QtCore.QRect(350, 70, 300, 61))
        self.NoteTitle.setFont(font)

        self.NoteTagslbl = QtWidgets.QLabel("Note tags", Frame)
        self.NoteTagslbl.setGeometry(QtCore.QRect(350, 150, 300, 61))
        self.NoteTagslbl.setFont(font)
        self.NoteTags = QtWidgets.QLineEdit(Frame)
        self.NoteTags.setGeometry(QtCore.QRect(350, 200, 300, 60))
        self.NoteTags.setFont(font)

        self.NoteBodylbl = QtWidgets.QLabel("Note Body", Frame)
        self.NoteBodylbl.setGeometry(QtCore.QRect(350, 300, 300, 61))
        self.NoteBodylbl.setFont(font)
        self.NoteBody = QtWidgets.QPlainTextEdit(Frame)
        self.NoteBody.setGeometry(QtCore.QRect(350, 350, 300, 300))
        self.NoteBody.setFont(font)

        jnote.title = self.NoteTitle.text()
        jnote.tags = self.NoteTags.text()
        jnote.body = self.NoteBody.toPlainText()

        self.saveNoteBtn = QtWidgets.QPushButton(Frame)
        self.saveNoteBtn.setObjectName("Save Note")
        self.saveNoteBtn.setGeometry(QtCore.QRect(350, 700, 300, 61))
        self.saveNoteBtn.clicked.connect(jhelp.add_Json_Note(jnote))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_app = TabWindow()
    main_app.initTabs(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
