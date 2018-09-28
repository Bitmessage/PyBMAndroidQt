import sys
import xmlrpc.client
import base64
import pickle
import logging
import json
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QPushButton,QDialog,QFormLayout,QGraphicsDropShadowEffect,
                     QHBoxLayout,QTabWidget,QMessageBox,QToolBar,QProgressBar,
                     QFrame,QGridLayout,QSizePolicy, QSpacerItem, QToolButton,QCompleter,
                     QVBoxLayout,QMenuBar,QStyleFactory,QMainWindow, QWidget, QTextEdit,
                     QLineEdit,QToolButton,QAction,QSplitter,QComboBox,QFileDialog,QPlainTextEdit,
                     QTableWidgetItem, QRadioButton,QLabel,QTableWidget,QListWidget,QListWidgetItem)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QSize, QRect,Qt
from PyQt5.QtGui import QRegExpValidator,QIcon, QPixmap, QColor

class ToolBars(QWidget):
    def __init__ (self):
        super(ToolBars, self).__init__()
        self.tools = QToolBar()
        self.tools.showMaximized()
        self.toolbar = QToolButton()
        self.toolbar.showMaximized()
        self.toolbar.setIcon(QIcon("images/images.png"))
        # self.toolbar.setIconSize(QSize(800,800))
        self.toolbar.setPopupMode(QToolButton.InstantPopup)
        self.toolbar.setAutoRaise( True )
        self.toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolbar.setCheckable( True )
        self.tools.addWidget(self.toolbar)
        self.toolbar.setFixedSize(100,100)

        self.inbox = QAction(QIcon("images/sign.png"),"Inbox",self)
        self.sends = QAction(QIcon("images/sign.png"),"Send",self)
        self.create = QAction(QIcon("images/sign.png"),"Create",self)
        self.trash = QAction(QIcon("images/sign.png"),"Trash",self)
        self.draft = QAction(QIcon("images/sign.png"),"Draft",self)
        self.toolbar.addAction(self.inbox)
        self.toolbar.addAction(self.create)
        self.toolbar.addAction(self.sends)
        self.toolbar.addAction(self.trash)
        self.toolbar.addAction(self.draft)
        self.tools.setStyleSheet('''
            color: rgb(0, 0, 255);
            font-size: 100;
            font-weight: 1000;
        ''')
        self.toolbar.setStyleSheet('''
            background-color: rgb(255, 0, 0);
        ''')


        self.combo=QComboBox()
        self.combo.setMaximumWidth(800)
        self.combo.setFixedHeight(200)
        ides = api.listAddresses()
        new_ides = json.loads(ides)
        list_ides = new_ides['addresses']
        list_com = []
        for address in list_ides:
            ids = address['address']
            labels = address['label']
            add_label2 = labels +"<"+ids+">"
            self.combo.addItem(add_label2)
        self.tools.addWidget(self.combo)



class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(255, 0, 0);
        ''')

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setIcon(self, imagePath):
        self.iconQLabel.setPixmap(QPixmap(imagePath))

    def cleared(self):
        item = self.allQHBoxLayout
        if item != None :
            widget = item.widget()
            if widget != None:
                self.allQHBoxLayout.removeWidget(widget)
                widget.deleteLater() 

class TrashWindow(ToolBars):
    def __init__(self, parent=None):
        super(TrashWindow, self).__init__()
        self.widget = QWidget(self)

        fbox = QFormLayout(self)
        fbox.addRow(self.tools)

        l1 = QLabel("To: ",self)
        self.add1 = QLineEdit(self)
        self.add1.setText("BM-2cWyUfBdY2FbgyuCb7abFZ49JYxSzUhNFe")
        fbox.addRow(l1,self.add1)

        l2 = QLabel("From: ",self)
        self.add2 = QLineEdit()
        self.add2.setText("BM-2cV5v5bqzVznBXk3fsLaAfPkCnC42Dhwc4")
        fbox.addRow(l2,self.add2)

class DraftWindow(ToolBars):
    def __init__(self, parent=None):
        super(DraftWindow, self).__init__()
        fbox = QVBoxLayout(self)    
        fbox.addWidget(self.tools)

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.showMaximized()
        for name, message, icon in [
            ('Meyoko', 'hello...',  'images/sign.png'),
            ('Nyaruko', 'how are you..', 'images/sign.png'),
            ('Louise', 'Dear friend',  'images/sign.png'),
            ('mily', 'hello...',  'images/sign.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(name)
            myQCustomQWidget.setTextDown(message)
            myQCustomQWidget.setIcon(icon)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            fbox.removeWidget(self.myQListWidget)
        fbox.addWidget(self.myQListWidget)

class CreateWindow(ToolBars):
    def __init__(self, parent=None):
        super(CreateWindow, self).__init__()
        self.widget = QWidget(self)
        fbox = QFormLayout(self)
        fbox.addRow(self.tools)

        l1 = QLabel("To: ",self)
        self.add1 = QComboBox(self)
        self.add1.setMaximumWidth(800)
        self.add1.setFixedHeight(100)
        self.add1.setCurrentText('choose')
        self.add1.currentTextChanged.connect(self.selectionchange)
        to_add = api.listAddressBookEntries()
        new_to = json.loads(to_add)
        list_to = new_to['addresses']
        for address in list_to:
            add1 = address['address']
            label1 = base64.b64decode(address['label']).decode("utf-8")
            add_label1 = label1 +"<"+add1+">"
            self.add1.addItem(add_label1)
        fbox.addRow(l1,self.add1)

        l2 = QLabel("From: ",self)
        self.add2 = QComboBox()
        self.add2.setMaximumWidth(800)
        self.add2.setFixedHeight(100)
        self.add2.setCurrentText('choose')
        self.add2.currentTextChanged.connect(self.selectionchange1)
        from_add = api.listAddresses()
        new_from = json.loads(from_add)
        list_from = new_from['addresses']
        for address in list_from:
            add2 = address['address']
            label2 = address['label']
            add_label2 = label2 +"<"+add2+">"
            self.add2.addItem(add_label2)
        fbox.addRow(l2,self.add2)

        l4 = QLabel("Subject: ",self)
        self.add4 = QLineEdit(self)
        fbox.addRow(l4,self.add4)

        l3 = QLabel("Message: ",self)
        fbox.addRow(l3)
        self.add3 = QTextEdit()
        fbox.addRow(self.add3)

        self.send = QPushButton(self)
        self.send.setText("SEND")
        self.send.clicked.connect(self.addition)
        fbox.addRow(self.send)

    def selectionchange1(self,i):
        sub = i[i.find('<')+1:i.find('>')]
        self.fromAddress = sub

    def selectionchange(self,i):
        sub = i[i.find('<')+1:i.find('>')]
        self.toAddress = sub

    def addition(self):
        subject = base64.b64encode(bytes(self.add4.text(), 'utf-8')).decode("utf-8")
        message = base64.b64encode(bytes(self.add3.toPlainText(), 'utf-8')).decode("utf-8")
        sums = api.sendMessage(self.toAddress, self.fromAddress, subject, message)
    

class InboxWindow(ToolBars):
    def __init__(self, parent=None,is_change= None,id_default = "BM-2cXtYXvA1yZ1KdjHufxqDEGPwd3Xt4JEdk"):
        super(InboxWindow, self).__init__()
        self.widget = QWidget(self)

        fbox = QVBoxLayout(self)    
        fbox.addWidget(self.tools)
        if is_change is not None:
            self.combo.clear()
            self.combo.addItem(is_change)
            ides = api.listAddresses()
            new_ides = json.loads(ides)
            list_ides = new_ides['addresses']
            list_com = []
            for address in list_ides:
                ids = address['address']
                labels = address['label']
                add_label2 = labels +"<"+ids+">"
                if is_change != add_label2:
                    self.combo.addItem(add_label2)
        else:
            pass

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.showMaximized()
        newids = base64.b64encode(bytes(id_default, 'utf-8')).decode("utf-8")
        messages = api.getInboxMessagesByAddress(id_default)
        new_messages = json.loads(messages)
        inbox_list = new_messages['inboxMessages']

        for inbox in inbox_list:
            add_from = inbox['fromAddress']
            subject = base64.b64decode(inbox['subject']).decode("utf-8")
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(add_from)
            myQCustomQWidget.setTextDown(subject)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        fbox.addWidget(self.myQListWidget)

class SendWindow(ToolBars):
    def __init__(self, parent=None,is_change= None,id_default = "BM-2cXtYXvA1yZ1KdjHufxqDEGPwd3Xt4JEdk"):
        super(SendWindow, self).__init__()
        self.widget = QWidget(self)

        fbox = QVBoxLayout(self) 
        fbox.addWidget(self.tools)
        if is_change is not None:
            self.combo.clear()
            self.combo.addItem(is_change)
            ides = api.listAddresses()
            new_ides = json.loads(ides)
            list_ides = new_ides['addresses']
            list_com = []
            for address in list_ides:
                ids = address['address']
                labels = address['label']
                add_label2 = labels +"<"+ids+">" 
                if is_change != add_label2:
                    self.combo.addItem(add_label2)
        else:
            pass

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setVisible(False)
        self.myQListWidget.setUpdatesEnabled(True)
        self.myQListWidget.showMaximized()
        messages = api.getSentMessagesByAddress(id_default)
        new_messages = json.loads(messages)
        inbox_list = new_messages['sentMessages']

        for inbox in inbox_list:
            add_from = inbox['toAddress']
            subject = base64.b64decode(inbox['subject']).decode("utf-8")
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(add_from)
            myQCustomQWidget.setTextDown(subject)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        fbox.addWidget(self.myQListWidget)
    
    
class UIToolTab(QWidget):
    def __init__(self, parent=None):
        super(UIToolTab, self).__init__()
        self.widget = QWidget(self)
        fbox = QFormLayout(self)
        fbox.setContentsMargins(100, 200, 100, 100)



        l1 = QLabel("Username: ",self)
        self.add1 = QLineEdit(self)
        fbox.addRow(l1,self.add1)

        l2 = QLabel("Password: ",self)
        self.add2 = QLineEdit(self)
        fbox.addRow(l2,self.add2)

        l4 = QLabel("IP Address: ",self)
        self.add4 = QLineEdit(self)
        fbox.addRow(l4,self.add4)

        l3 = QLabel("Port: ",self)
        self.add3 = QLineEdit(self)
        fbox.addRow(l3,self.add3)

        try:
            pickle_off = open("Credentials.json","r")
            emp = json.load(pickle_off)
            self.add1.setText(emp['username'])
            self.add2.setText(emp['password'])
            self.add4.setText(emp['ip'])
            self.add3.setText(emp['port'])
        except:
            pass

        self.connect = QPushButton(self)
        self.connect.setText("CONNECT")
        self.save = QPushButton(self)
        self.save.setText("SAVE")
        fbox.addRow(self.save,self.connect)
        

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.changes_menu = 'Inbox'
        self.ToolTab = UIToolTab(self)
        self.startUIToolTab()

    def startUIToolTab(self):
        self.setWindowTitle("CONNECT")
        self.setCentralWidget(self.ToolTab)
        self.ToolTab.connect.clicked.connect(self.verify)
        self.ToolTab.save.clicked.connect(self.save_data)
        self.show()

    def save_data(self):
        user = self.ToolTab.add1.text()
        password = self.ToolTab.add2.text()
        ip = self.ToolTab.add4.text()
        port = self.ToolTab.add3.text()
        emp = {'username':user,'password':password,'ip':ip,'port':port}
        credentials = open("Credentials.json","w")
        json.dump(emp, credentials)

    def verify(self):
        global api
        user = self.ToolTab.add1.text()
        password = self.ToolTab.add2.text()
        ip = self.ToolTab.add4.text()
        port = self.ToolTab.add3.text()
        api = xmlrpc.client.ServerProxy("http://%s:%s@%s:%s/" %(user,password,ip,port))
        sums = api.add(2,3)
        if isinstance(sums, int):
            self.startInbox()
        else:
            choice = QMessageBox.question(self, 'Incorrect',
                                            "You have Put Incorrect Credentials",
                                            QMessageBox.Yes)
            if choice == QMessageBox.Yes:
                self.ToolTab.add1.setText("")
                self.ToolTab.add2.setText("")
                self.ToolTab.add4.setText("")
                self.ToolTab.add3.setText("")
            

    def startInbox(self):
        self.Window = InboxWindow(self)
        self.setWindowTitle("Inbox")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()

    def startSend(self):
        self.Window = SendWindow(self)
        self.setWindowTitle("Send")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()

    def startCreate(self):
        self.Window = CreateWindow(self)
        self.setWindowTitle("Create")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()

    def startDraft(self):
        self.Window = DraftWindow(self)
        self.setWindowTitle("Draft")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()

    def startTrash(self):
        self.Window = TrashWindow(self)
        self.setWindowTitle("Trash")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()

    def changedItem(self,folder,comb):
        if folder == 'Inbox':
            self.Window = InboxWindow(self,is_change=comb,id_default = self.select_ids)
            self.setWindowTitle("Inbox")
        if folder == 'Send':
            self.Window = SendWindow(self,is_change=comb,id_default = self.select_ids)
            self.setWindowTitle("Send")
        self.setCentralWidget(self.Window)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))
        self.Window.toolbar.triggered[QAction].connect(self.toolbtnpressed)
        self.Window.combo.currentTextChanged.connect(self.selectionchange_id)
        self.show()


    def toolbtnpressed(self,a):
        if a.text() == 'Inbox':
            self.changes_menu = 'Inbox'
            self.startInbox()
        if a.text() == 'Create':
            self.startCreate()
        if a.text() == 'Send':
            self.changes_menu = 'Send'
            self.startSend()
        if a.text() == 'Draft':
            self.startDraft()
        if a.text() == 'Trash':
            self.startTrash()

    def selectionchange_id(self,ids):
        self.select_ids = ids[ids.find('<')+1:ids.find('>')]
        if self.changes_menu == 'Inbox':
            self.changedItem('Inbox',ids)

        if self.changes_menu == 'Send':
            self.changedItem('Send',ids)

        

if __name__ == '__main__':
    # logging.basicConfig(filename='/storage/emulated/0/example.txt',level=logging.INFO)
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())