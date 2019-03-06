# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5.QtWidgets import QAction, QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QMessageBox
import copy

app = QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
(screen_width, screen_height) = (size.width(), size.height())

f = open("pi_under_point.txt", "r")
pi_numbers = f.readline()
f.close()
pi_numbers = list(map(int, list(pi_numbers)))

def alert_message(origin, alert_name, alert_detail):
    """
    경고 창을 띄웁니다. 닫기 전엔 다른 걸 할 수 없습니다.
    :parameter origin: 이 경고창이 어디서 띄워지는지
    :parameter alert_name: 경고 창의 제목
    :parameter alert_detail: 경고 창 내용
    """
    msg = QMessageBox()  # 메시지 객체 생성
    msg.setIcon(QMessageBox.Critical)  # 아이콘: 빨간 X자
    msg.setWindowTitle(alert_name)  # 창 이름
    msg.setText(alert_detail)  # 창 내용
    msg.setStandardButtons(QMessageBox.Ok)  # 버튼 1개 추가: ok 버튼
    msg.exec_()  # 실행하기(이거 끄기 전에 못 끔)

class Wind(QWidget):
    def __init__(self, name):
        super().__init__()  # 상위 클래스의 생성자 호출
        self.name = name  # 창의 이름 정하기
        self.design()  # 디자인
        self.setup()  # 셋업

    def design(self):
        self.setFont(QFont("KoPub돋움체 Light", 48))  # 폰트 설정

    def setup(self):
        self.show()  # 창 보이기

    def closeEvent(self, QCloseEvent):
        QCloseEvent.ignore()  # CloseEvent 거절(못 닫도록)

    def refresh(self):
        self.update()


class Game_Wind(Wind):
    def __init__(self, name):
        self.index = 0  # 시스템 상: 맞추어야 하는 자리 수, 표시: 지금까지 맞춘 자리 수
        super().__init__(name)

    def design(self):
        # 레이아웃 꾸미기
        super().design()

        self.UpLayout = QHBoxLayout()
        self.MidLayout = QHBoxLayout()
        self.DownLayout = QHBoxLayout()
        self.TotalLayout = QVBoxLayout()
        self.info_text=Text("시작해주세요!", self)

        self.UpLayout.addStretch(1)
        self.UpLayout.addWidget(Text("원주율 π 외우기! (소수점 아래부터 쳐주세요)", self))
        self.UpLayout.addStretch(1)

        self.MidLayout.addStretch(1)
        self.MidLayout.addWidget(self.info_text)
        self.MidLayout.addStretch(1)

        self.TotalLayout.addStretch(2)
        self.TotalLayout.addLayout(self.UpLayout)
        self.TotalLayout.addLayout(self.MidLayout)
        self.TotalLayout.addStretch(1)
        self.TotalLayout.addLayout(self.DownLayout)
        self.TotalLayout.addStretch(2)

        self.setLayout(self.TotalLayout)

    def setup(self):
        self.setWindowTitle(self.name)
        self.showFullScreen()

    def keyPressEvent(self, QKeyEvent):
        Flag=False
        if QKeyEvent.key() == Qt.Key_0 or QKeyEvent.key() == Qt.Key_P:
            Flag=True
            if 0!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_1 or QKeyEvent.key() == Qt.Key_Q:
            Flag=True
            if 1!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_2 or QKeyEvent.key() == Qt.Key_W:
            Flag=True
            if 2!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_3 or QKeyEvent.key() == Qt.Key_E:
            Flag=True
            if 3!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_4 or QKeyEvent.key() == Qt.Key_R:
            Flag=True
            if 4!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_5 or QKeyEvent.key() == Qt.Key_T:
            Flag=True
            if 5!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_6 or QKeyEvent.key() == Qt.Key_Y:
            Flag=True
            if 6!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_7 or QKeyEvent.key() == Qt.Key_U:
            Flag=True
            if 7!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_8 or QKeyEvent.key() == Qt.Key_I:
            Flag=True
            if 8!=pi_numbers[self.index]:
                self.game_over()
                return
        elif QKeyEvent.key() == Qt.Key_9 or QKeyEvent.key() == Qt.Key_O:
            Flag=True
            if 9!=pi_numbers[self.index]:
                self.game_over()
                return
        if Flag:
            self.info_text.setText("마지막으로 누른 키: "+str(pi_numbers[self.index]))
            self.index+=1
        else:
            self.info_text.setText("제대로 눌러주세요.")
        self.refresh()

    def game_over(self):
        alert_message(self,"오답!","정답은 "+str(pi_numbers[self.index])+"입니다.\n당신의 점수: "+str(self.index))
        self.index=0
        self.info_text.setText("시작해주세요!")
        self.refresh()

class Text(QLabel):
    def __init__(self, text, window):
        super().__init__(text, window)  # 상위 클래스의 생성자 호출

    def setup(self):
        # 텍스트를 세팅하고 띄웁니다. 크기는 글자에 맞추어 고정됩니다.
        self.setFixedSize(self.sizeHint())  # 크기 설정
        self.show()


intro = Game_Wind("Pi Memorizing")
sys.exit(app.exec_())
