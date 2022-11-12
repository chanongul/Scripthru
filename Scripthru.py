import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Scripthru(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("scth.ico"))
        self.setWindowTitle("Scripthru")
        self.setWindowFlags(
            self.windowFlags()
            | QtCore.Qt.WindowType.FramelessWindowHint
            | QtCore.Qt.WindowStaysOnTopHint
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet(
            """
        #background {
            background-color: rgba(255,255,255,100);
            border-radius: 5px;
            border-style: solid;
            border-color: #dddddd;
            border-width: 0.5px;
        }
        #min, #exit {
            background-color: rgba(225,225,225,100);
            color: #dddddd;
            border-radius: 10px;
        }
        #min::hover {
            background-color: yellow;
            color: black;
        }
        #exit::hover {
            background-color: red;
            color: white;
        }
        #scrollArea, #text, #textEdit {
            background: transparent;
        }
        """
        )
        self.setObjectName("scripthru")
        self.resize(1000, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(1000, 600))
        self.setMaximumSize(QtCore.QSize(1000, 600))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.background = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setMinimumSize(QtCore.QSize(1000, 600))
        self.background.setMaximumSize(QtCore.QSize(1000, 600))
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 7, 5)
        self.verticalLayout.setSpacing(0)
        self.nav = QtWidgets.QHBoxLayout()
        self.nav.setObjectName("nav")
        self.nav.setSpacing(5)
        self.logo = QtWidgets.QLabel(self.background)
        self.logo.setObjectName("logo")
        self.nav.addWidget(self.logo)
        self.min = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.min.sizePolicy().hasHeightForWidth())
        self.min.setSizePolicy(sizePolicy)
        self.min.setMinimumSize(QtCore.QSize(20, 20))
        self.min.setMaximumSize(QtCore.QSize(20, 20))
        self.min.setObjectName("min")
        self.nav.addWidget(self.min)
        self.exit = QtWidgets.QPushButton(self.background)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exit.sizePolicy().hasHeightForWidth())
        self.exit.setSizePolicy(sizePolicy)
        self.exit.setMinimumSize(QtCore.QSize(20, 20))
        self.exit.setMaximumSize(QtCore.QSize(20, 20))
        self.exit.setObjectName("exit")
        self.nav.addWidget(self.exit)
        self.verticalLayout.addLayout(self.nav)
        self.text = QtWidgets.QWidget()
        self.text.setObjectName("text")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.text)
        self.gridLayout_2.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.text)
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_2.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.text)
        self.config = QtWidgets.QHBoxLayout()
        self.config.setContentsMargins(0, 0, -1, -1)
        self.config.setObjectName("config")
        self.opacity = QtWidgets.QSlider(self.background)
        self.opacity.setMaximumSize(QtCore.QSize(200, 50))
        self.opacity.setMinimum(10)
        self.opacity.setMaximum(250)
        self.opacity.setProperty("value", 100)
        self.opacity.setOrientation(QtCore.Qt.Horizontal)
        self.opacity.setInvertedAppearance(False)
        self.opacity.setInvertedControls(False)
        self.opacity.setObjectName("opacity")
        self.config.addWidget(self.opacity)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.config.addItem(spacerItem)
        self.font = QtWidgets.QPushButton(self.background)
        self.font.setObjectName("font")
        self.config.addWidget(self.font)
        self.color = QtWidgets.QPushButton(self.background)
        self.color.setObjectName("color")
        self.config.addWidget(self.color)
        self.verticalLayout.addLayout(self.config)
        self.gridLayout.addWidget(self.background, 0, 0, 1, 1)
        self.logo.setText("Scripthru")
        self.exit.setText("x")
        self.min.setText("-")
        self.font.setText("Edit Font")
        self.color.setText("Edit Color")
        self.min.clicked.connect(self.minWindow)
        self.exit.clicked.connect(self.exitWindow)
        self.font.clicked.connect(self.setFont)
        self.color.clicked.connect(self.setFontColor)
        self.opacity.valueChanged.connect(self.setOpacity)
        self.logo.mouseMoveEvent = self.moveWithNav

    def mousePressEvent(self, event):
        self.cur_pos = event.globalPos()

    def moveWithNav(self, event):
        if not self.isMaximized():
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.cur_pos)
                self.cur_pos = event.globalPos()

    def minWindow(self):
        self.setWindowState(QtCore.Qt.WindowState.WindowMinimized)

    def exitWindow(self):
        sys.exit(0)

    def setOpacity(self, val):
        self.background.setStyleSheet(
            "#background { background-color: rgba(255,255,255," + str(val) + "); }"
        )

    def setFont(self):
        self.hide()
        font, ok = QtWidgets.QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)
        self.show()

    def setFontColor(self):
        self.hide()
        color = QtWidgets.QColorDialog.getColor().name()
        self.textEdit.setStyleSheet("#textEdit { color: " + color + "}")
        self.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    gui = Scripthru()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
