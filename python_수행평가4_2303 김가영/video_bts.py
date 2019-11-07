from tkinter import *
from bts_1 import Bts_1
from bts_2 import Bts_2

class Video_bts:
    def Bts_1(self):
        bts_1 = Bts_1()
        print("방탄소년단 공연영상입니다 !")
        open(file="bts_1.py")

    def Bts_2(self):
        bts_2 = Bts_2()
        print("방탄소년단 정식촬영영상입니다 !")
        open(file="bts_2.py")

    def __init__(self):

        self.root = Toplevel()

        self.root.title("Kind_Video")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/videokind.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=25, height=15, text="공연영상", overrelief="solid", bg='white', command=self.Bts_1)
        self.button1.place(x=150, y=175)

        self.button2 = Button(self.root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white', command=self.Bts_2)
        self.button2.place(x=370, y=175)


        self.root.mainloop()