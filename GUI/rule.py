import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Rule_dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.rule()

    def rule(self):
        # Ok버튼
        Okbtn = QPushButton("OK", self)
        # Okbtn.setGeometry(450, 565, 100, 100)
        Okbtn.clicked.connect(self.rule_close)

        #Title
        labelTitle = QLabel('게임규칙')
        labelTitle.setAlignment(Qt.AlignHCenter)

        #내용
        labelContents1 = QLabel('- 서로 번갈아가며 주사위를 돌리고 주사위에 나온 숫자만큼 앞으로 이동합니다')
        labelContents2 = QLabel('- 상대방 소유에 land에 도착하게 되면 life를 하나 잃게 됩니다')
        labelContents3 = QLabel('- map을 한바퀴 완주하게 되면 life를 하나 얻습니다')
        labelContents4 = QLabel('- Specialplace1(무인도)')
        labelContents5 = QLabel('무인도에 도착하면 3턴동안 이동 할 수 없습니다')
        labelContents6 = QLabel('- Specialplace2(폭풍우)')
        labelContents7 = QLabel('폭풍우를 만나게 되면 임의에 land로 날아가게 됩니다')
        labelContents8 = QLabel('- 게임종료')
        labelContents9 = QLabel('두 팀중 life 값이 0이 먼저 되는 팀이 패배하게 됩니다')

        labelContents1.setAlignment(Qt.AlignLeft)
        labelContents2.setAlignment(Qt.AlignLeft)
        labelContents3.setAlignment(Qt.AlignLeft)
        labelContents4.setAlignment(Qt.AlignLeft)
        labelContents5.setAlignment(Qt.AlignLeft)
        labelContents6.setAlignment(Qt.AlignLeft)
        labelContents7.setAlignment(Qt.AlignLeft)
        labelContents8.setAlignment(Qt.AlignLeft)
        labelContents9.setAlignment(Qt.AlignLeft)

        #폰트
        font1 = labelTitle.font()
        font1.setPointSize(15)
        font1.setBold(True)

        font2 = labelContents1.font()
        font2.setPointSize(10)

        #폰트 적용
        labelTitle.setFont(font1)
        labelContents1.setFont(font2)
        labelContents2.setFont(font2)
        labelContents3.setFont(font2)
        labelContents4.setFont(font2)
        labelContents5.setFont(font2)
        labelContents6.setFont(font2)
        labelContents7.setFont(font2)
        labelContents8.setFont(font2)
        labelContents9.setFont(font2)

        #label 사용
        layout = QVBoxLayout()
        layout.addWidget(labelTitle)
        layout.addWidget(labelContents1)
        layout.addWidget(labelContents2)
        layout.addWidget(labelContents3)
        layout.addWidget(labelContents4)
        layout.addWidget(labelContents5)
        layout.addWidget(labelContents6)
        layout.addWidget(labelContents7)
        layout.addWidget(labelContents8)
        layout.addWidget(labelContents9)
        layout.addWidget(Okbtn)

        self.setLayout(layout)

        self.setWindowTitle('Rule')
        self.setWindowIcon(QIcon('../_image/dice_roll.gif'))
        self.setWindowModality(Qt.ApplicationModal)
        self.resize(1000, 600)
        self.show()

    #버튼 클릭후 종료
    def rule_close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Rul = Rule_dialog()
    Rul.show()
    app.exec_()


