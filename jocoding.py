import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
# from GUI.result import ResultScreen

# 첫번째 화면 시작하기, 선택하면 두번째 화면 실행
class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        from test1 import Bigtext
        big = Bigtext(0)
        for i in range(5):
            text += "{}  {}  {}         {}  {}  {}  {}\n".format(bigY.get_line(i), bigO.get_line(i), bigU.get_line(i),
                                                    bigL.get_line(i), bigO.get_line(i), bigS.get_line(i),
                                                    bigE.get_line(i))
        ending_text = big.show_text()
        label = QLabel(ending_text, self)
        label.setGeometry(0, 200, 400, 100)
        # label.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("test")
        self.setGeometry(500, 500, 500, 500)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = FirstWindow()
    start.show()
    app.exec_()
