# !/urs/bin/python3
# -*- coding: utf-8 -*-

import sys, time

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
import pyautogui as pg


class App(QWidget):

    def __init__(self):
        self.start()
        self.set()

    def start(self):
        self.ui = uic.loadUi('ui.ui')
        self.ui.show()

    def set(self):
        self.ui.btnStart.clicked.connect(lambda: self.gogogo())
        self.ui.lineHowMatch.setValidator(QIntValidator())

    def gogogo(self):
        q = 0
        е = 0
        while True:
            while q < int(self.ui.lineHowMatch.text()):
                try:
                    print(q, self.ui.lineHowMatch.text())
                    location = pg.locateOnScreen('again.png', confidence=0.8)
                    point = pg.center(location)
                    x, y = point
                    pg.click(x, y)
                    q += 1
                    self.ui.lineCount.setText(q)
                except:
                    е += 1
                    time.sleep(5)
                    print(е)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()