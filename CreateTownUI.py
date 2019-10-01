#!/usr/bin/python
# -'''- coding: utf-8 -'''-

import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QCheckBox)
import GeneratorHelpers as GenHelp
import Helpers as hlp
import TownGenerator as tog
import json
import pickle


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.TownName = QLineEdit("TownName")
        self.PopulationSize = QLineEdit("PopulationSize")
        self.HowManyNpcsToGenerate = QLineEdit("HowManyNpcsToGenerate")
        self.GenerateMerchants = QCheckBox("GenerateMerchants")
        self.button = QPushButton("Show Greetings")


        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.TownName)
        layout.addWidget(self.PopulationSize)
        layout.addWidget(self.HowManyNpcsToGenerate)
        layout.addWidget(self.GenerateMerchants)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.CreateTown)

    # Greets the user
    def CreateTown(self):

        gencharsnum = int(self.HowManyNpcsToGenerate.text())
        GH = GenHelp.GeneratorHelpers()
        HP = hlp.Helpers()
        TG = tog.Town_blank()

        TG.TownName = self.TownName.text()
        TG.HowManyNpcsToGenerate = self.HowManyNpcsToGenerate.text()
        TG.PopulationSize = self.PopulationSize.text()
        TG.GenerateMerchants = self.GenerateMerchants.isChecked()
        TG.Npc_obj = GH.create_char_ob(gencharsnum)
        HP.save_out_picklefile(TG, "TownData.TD")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())