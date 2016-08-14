import sys
from orbital import *
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "hohmann_gui.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class orbital_main(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Connect the Orbit 1 Buttons
        self.tool_button_circle_1.clicked.connect(self.display_1_0)
        self.tool_button_ellipse_1.clicked.connect(self.display_1_1)
        self.tool_button_hyperbola_1.clicked.connect(self.display_1_2)

        # Connect the Orbit 2 Buttons
        self.tool_button_circle_2.clicked.connect(self.display_2_0)
        self.tool_button_ellipse_2.clicked.connect(self.display_2_1)
        self.tool_button_hyperbola_2.clicked.connect(self.display_2_2)

        self.tool_button_run.clicked.connect(self.run_orbital)

    def display_1_0(self):
        self.stackedWidget.setCurrentIndex(0)

    def display_1_1(self):
        self.stackedWidget.setCurrentIndex(1)

    def display_1_2(self):
        self.stackedWidget.setCurrentIndex(2)

    def display_2_0(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def display_2_1(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def display_2_2(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def run_orbital(self):
        self.planet = self.combo_box_planet.currentText()
        orbit1 = Orbit(self.planet, radPeriapsis=5000.0, radApoapsis=5000.0, inclination=28.5)
        orbit2 = Orbit(self.planet, radPeriapsis=10000.0, radApoapsis=10000.0, inclination=28.5)
        DVtot, DV1, DV2 = orbit1.hohmann(orbit2)
        #        print(DVtot, DV1, DV2)
        DVtot = '%.3f km/s' % DVtot
        DV1 = '%.3f km/s' % DV1
        DV2 = '%.3f km/s' % DV2
        #        print(DVtot, DV1, DV2)
        self.line_edit_out_1.setText(DVtot)
        self.line_edit_out_2.setText(DV1)
        self.line_edit_out_3.setText(DV2)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = orbital_main()
    window.show()
    sys.exit(app.exec_())
