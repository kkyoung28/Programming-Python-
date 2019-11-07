#2
from tkinter import *
from kpop import Kpop
from tkinter import messagebox as msg


class Kind:
    # '준비중입니다' 메세지 박스 띄우는 함수
    def fbutton1(self):
        msg.showwarning('pop', '아직 준비중입니다!')

    def fbutton2(self):
        msg.showwarning('Girls Hiphop', '아직 준비중입니다!')

    def fbutton3(self):
        msg.showwarning('House', '아직 준비중입니다!')

    def fbutton4(self):
        msg.showwarning('Urban', '아직 준비중입니다!')

    def fbutton5(self):
        msg.showwarning('B-boy', '아직 준비중입니다!')

    def Kpop(self):
        kpop = Kpop()
        print("원하는 그룹을 선택하세요!")
        open(file="kpop.py")

    def __init__(self):
        self.root = Toplevel()

        self.root.title("Dance_Kind")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/kind.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="K-pop", overrelief="solid", bg='salmon', command=self.Kpop)
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="pop", overrelief="solid", bg='sandybrown', command=self.fbutton1)
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="Girls Hiphop", overrelief="solid", bg='yellow', command=self.fbutton2)
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="House", overrelief="solid", bg='lightgreen', command=self.fbutton3)
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="Urban", overrelief="solid", bg='skyblue', command=self.fbutton4)
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="B-boy", overrelief="solid", bg='palevioletred', command=self.fbutton5)
        self.button6.place(x=460, y=310)

        self.root.mainloop()

