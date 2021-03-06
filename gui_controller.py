import sys
from PyQt5 import QtWidgets
from model import Model
from view import QtView


class GuiController(QtView):
    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QWidget()
        self.setupUi(window)
        window.show()
        sys.exit(app.exec_())

    def fill_desc(self):
        self.model.desc_size = self.spinBox.value()
        self.model.knights_num = self.spinBox_2.value()
        self.model.create_desc_html()
        self.textBrowser.setHtml(self.model.desc_html)


if __name__ == "__main__":
    GuiController(Model()).start()
