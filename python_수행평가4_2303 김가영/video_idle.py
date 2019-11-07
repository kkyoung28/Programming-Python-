from tkinter import *
from idle_1 import Idle_1
from idle_2 import Idle_2

class Video_idle:
    def Idle_1(self):
        idle_1 = Idle_1()
        print("(여자)아이들 공연영상입니다 !")
        open(file="idle_1.py")

    def Idle_2(self):
        idle_2 = Idle_2()
        print("(여자)아이들 정식촬영영상입니다 !")
        open(file="idle_2.py")

    def __init__(self):

        self.root = Toplevel()

        self.root.title("Kind_Video")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/videokind.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=25, height=15, text="공연영상", overrelief="solid", bg='white', command=self.Idle_1)
        self.button1.place(x=150, y=175)

        self.button2 = Button(self.root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white', command=self.Idle_2)
        self.button2.place(x=370, y=175)


        self.root.mainloop()