import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import randint
from menu.menu import Menu

CalUI = 'e:/random_dice/mymodify/_guiFiles/frame.ui'


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self, None)
        uic.loadUi(CalUI, self)

        self.dice_pushButton.clicked.connect(self.dice)

    def initUI(self):
        label1 = QLabel

    def dice(self):
        result = randint(1, 6)
        print(result)
        return result

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainDialog = MainDialog()
    mainDialog.show()
    app.exec_()

    while True:
        input_start = input("사용하실 메뉴를 골라주세요.\n1.시작하기\n2.불러오기\n3.나가기\n")

        new_menu = Menu(input_start)

        if new_menu.now_page == "1":
            new_menu.page1()
        elif new_menu.now_page == "2":
            new_menu.page2()
        elif new_menu.now_page == "3":
            print("종료합니다.")
            break



