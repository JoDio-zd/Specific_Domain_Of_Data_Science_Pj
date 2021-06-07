import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QTextEdit,QAction, QFileDialog, QApplication, QPushButton, QWidget, QGridLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from backend import uploadphoto

class MainUi(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setFixedSize(960, 700)
        self.main_widget = QWidget() 
        self.main_layout = QGridLayout()
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QGridLayout()
        self.left_widget.setLayout(self.left_layout)

        self.right_widget = QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        self.button1 = QPushButton(QIcon(''), '打开文件')
        self.left_layout.addWidget(self.button1, 2, 0, 1, 3)
        self.label = QLabel()
        self.right_layout.addWidget(self.label, 0, 0, 4, 8)
        self.button1.clicked.connect(self.showDialog1)
        

    def showDialog1(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;*.jpeg;;All Files(*)")
        jpg = QPixmap(imgName).scaled(self.label.width(), self.label.height(), aspectRatioMode=Qt.KeepAspectRatio)
        self.label.setPixmap(jpg)
        print(imgName)
        upload1 = uploadphoto()
        upload1.uploadfile_to_server(imgName)
        upload1.exec()
        upload1.download(imgName)

def main():
    app = QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
