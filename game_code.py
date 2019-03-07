# -*- coding:utf-8 -*-
import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5.QtWidgets import QAction, QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QMessageBox

f = open("pi_under_point.txt", "r")
pi_numbers = f.readline()
f.close()
pi_numbers = list(map(int, list(pi_numbers)))

def alert_message(origin, alert_name, alert_detail):
    msg = QMessageBox()  # 메시지 객체 생성
    msg.setIcon(QMessageBox.Critical)  # 아이콘: 빨간 X자
    msg.setWindowTitle(alert_name)  # 창 이름
    msg.setText(alert_detail)  # 창 내용
    msg.setStandardButtons(QMessageBox.Ok)  # 버튼 1개 추가: ok 버튼
    msg.exec_()  # 실행하기(이거 끄기 전에 못 끔)

def text_to_layout_center(layout, text):
    layout.addStretch(1)
    layout.addWidget(text)
    layout.addStretch(1)

class Wind(QWidget):
    def __init__(self, name):
        super().__init__()  # 상위 클래스의 생성자 호출
        self.name = name  # 창의 이름 정하기
        self.design()  # 디자인
        self.setup()  # 셋업

    def design(self):
        self.setFont(QFont("조선일보명조", 48))  # 폰트 설정

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

        self.TitleLayout = QHBoxLayout()
        self.InfoLayout = QHBoxLayout()
        self.RecordLayout = QHBoxLayout()
        self.TotalLayout = QVBoxLayout()

        self.info_text=Text("시작하십시오. (소수점 아래부터)", self)
        self.record_string="3."
        self.record_text = Text(self.record_string,self)

        text_to_layout_center(self.TitleLayout, Text("원주율 π 외우기", self))
        text_to_layout_center(self.InfoLayout, self.info_text)
        text_to_layout_center(self.RecordLayout, self.record_text)

        self.TotalLayout.addStretch(2)
        self.TotalLayout.addLayout(self.TitleLayout)
        self.TotalLayout.addLayout(self.InfoLayout)
        self.TotalLayout.addStretch(1)
        self.TotalLayout.addLayout(self.RecordLayout)
        self.TotalLayout.addStretch(2)

        self.setLayout(self.TotalLayout)

    def setup(self):
        self.setWindowTitle(self.name)
        self.showFullScreen()

    def keyPressEvent(self, QKeyEvent):
        Flag=False
        keyPressed=QKeyEvent.key()-Qt.Key_0 # 0부터 9까지는 순서대로 있어서 이렇게 가능
        if 0<=keyPressed<=9:
            Flag=True
            if keyPressed!=pi_numbers[self.index]:
                self.game_over()
                return
                
        if Flag:
            self.info_text.setText("")
            self.record_update(keyPressed)
            self.index+=1
        else:
            self.info_text.setText("제대로 눌러주십시오...")
        self.refresh()

    def record_update(self, keyPressed):
        if self.index%6==0:
            if len(self.record_string)>=30:
                self.record_string=self.record_string[1:]+" "
            else:
                self.record_string+=" "
        if len(self.record_string)>=30:
            self.record_string=self.record_string[1:]+str(keyPressed)
        else:
            self.record_string+=str(keyPressed)
        self.record_text.setText(self.record_string)

    def game_over(self):
        alert_message(self,"오답!","정답은 "+str(pi_numbers[self.index])+"입니다.\n당신의 점수: "+str(self.index))
        self.index=0
        self.info_text.setText("시작하십시오. (소수점 아래부터)")
        self.record_string="3."
        self.record_text.setText(self.record_string)
        self.refresh()

class Text(QLabel):
    def __init__(self, text, window):
        super().__init__(text, window)  # 상위 클래스의 생성자 호출

    def setup(self):
        # 텍스트를 세팅하고 띄웁니다. 크기는 글자에 맞추어 고정됩니다.
        self.setFixedSize(self.sizeHint())  # 크기 설정
        self.show()

app = QApplication(sys.argv)
intro = Game_Wind("Pi Memorizing")
sys.exit(app.exec_())
