import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# import circular progress
from circular_progress import CircularProgress


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # resize window
        self.resize(500, 500)

        #remove title bar
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # create container and layout
        self.container = QFrame()
        self.container.setStyleSheet("background-color: transparent")
        self.layout = QVBoxLayout()

        # create circular progress
        self.progress = CircularProgress()
        self.progress.value = 50
        self.progress.suffix="%"
        self.progress.font_size = 12
        self.progress.width=300
        self.progress.height=300
        self.progress.progress_width=10
        self.progress.text_color=0xFFFFFF
        self.progress.progress_color=0xFFFFFF
        self.progress.progress_rounded_cap=True
        self.progress.add_shadow(True)
        self.progress.setMinimumSize(self.progress.width, self.progress.height)

        # add slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 100)
        self.slider.valueChanged.connect(self.change_value)

        # add widgets
        self.layout.addWidget(self.progress, Qt.AlignCenter, Qt.AlignCenter)
        self.layout.addWidget(self.slider, Qt.AlignCenter, Qt.AlignCenter)

        # set central widget
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        # show window
        self.show()

    #change value
    def change_value(self, value):
        self.progress.set_value(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
