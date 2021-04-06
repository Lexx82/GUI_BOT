import sys, time
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QLineEdit, QLabel, QProgressBar, QVBoxLayout
from PyQt5.QtCore import Qt, QThread


class ProgressBarThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        value = self.mainwindow.progressBar.value()
        while value < int(self.mainwindow.lineEdit.text()):
            value += 1
            self.mainwindow.progressBar.setValue(value)
            time.sleep(10)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.btnStart = QPushButton('Начать геноцид')
        self.lblHM = QLabel('Сколько боев провести?')
        self.lineEdit = QLineEdit()
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.setGeometry(300, 200, 300, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lblHM)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(self.btnStart)
        vbox.addWidget(self.progressBar)
        self.setLayout(vbox)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
