import sys
from PySide import QtGui
import re

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))

        self.show()
        dummy = 'GoulartDoucetSantamariaTitianaVerunaLauranaMilderHarvenheitArcoBrazenAndreevBellevilleEiichiroPlainviewLauberBadaDarltonLowsleyBreedingAugeasPrinceyCaskettGillinghamShiroiGreaneArkhanEliwoodKrummYavannaJaganshiShannenGettsVerreSimonovaGeorgioCronaOhlinRudetskyTreewayArianrodaTibbettMirellaDarrowsArmoniaStefanovicHadsonBillerSolanDavittKorosuLaxusBarettMinajiSenkoMihailovNodaHinagikuDineenHerseyWhittinghamTalinaCrosGrestMontandEiichiroMckellanDarksonMitamaPuppingtonMurakiTarikGoudlingHausmannThoreFogelburgOvendenSonadaKellumZabatAugerLaycockEncantoGluckBurgenDelaireGoodladySkrullRykoNarglesGuildensternWinnifredVasilovHilterSidanKotaroCorenthos'
        print(re.findall('[A-Z][^A-Z]*', dummy))



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()