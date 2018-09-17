import xmlrpc.client
import sys
import base64
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QApplication, QPushButton,QFormLayout,QMainWindow, QWidget, QLabel, QLineEdit, QPlainTextEdit
from PyQt5.QtGui import QRegExpValidator

class Addition(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.widget = QWidget()
        fbox = QFormLayout()

        l1 = QLabel("TO: ")
        self.add1 = QLineEdit()
        self.add1.setText("BM-2cWyUfBdY2FbgyuCb7abFZ49JYxSzUhNFe")
        self.add1.setReadOnly(True)
        fbox.addRow(l1,self.add1)

        l2 = QLabel("FROM: ")
        self.add2 = QLineEdit()
        self.add2.setText("BM-2cV5v5bqzVznBXk3fsLaAfPkCnC42Dhwc4")
        self.add2.setReadOnly(True)
        fbox.addRow(l2,self.add2)

        l4 = QLabel("SUBJECT: ")
        self.add4 = QLineEdit()
        fbox.addRow(l4,self.add4)

        l3 = QLabel("MESSAGE: ")
        self.add3 = QPlainTextEdit()
        fbox.addRow(l3,self.add3)

        b = QPushButton()
        b.setText("SEND")
        b.clicked.connect(self.addition)
        fbox.addRow(b)


        self.widget.setLayout(fbox)
        self.widget.show()
        self.setCentralWidget(self.widget)
        self.setWindowTitle("SEND")

    def addition(self):
        fromAddress = self.add2.text()
        toAddress = self.add1.text()
        subject = base64.b64encode(bytes(self.add4.text(), 'utf-8')).decode("utf-8")
        message = base64.b64encode(bytes(self.add3.toPlainText(), 'utf-8')).decode("utf-8")
        api = xmlrpc.client.ServerProxy("http://username:password@127.0.0.1:8442/")
        sums = str(api.sendMessage(toAddress, fromAddress, subject, message))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apps = Addition()
    apps.show()
    sys.exit(app.exec_())