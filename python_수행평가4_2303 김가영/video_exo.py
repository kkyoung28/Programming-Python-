from tkinter import *
from exo_1 import Exo_1
from exo_2 import Exo_2

class Video_exo:
    def Exo_1(self):
        exo_1 = Exo_1()
        print("엑소 공연영상입니다 !")
        open(file="exo_1.py")

    def Exo_2(self):
        exo_2 = Exo_2()
        print("엑소 정식촬영영상입니다 !")
        open(file="exo_2.py")

    def __init__(self):

        self.root = Toplevel()

        self.root.title("Kind_Video")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/videokind.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=25, height=15, text="공연영상", overrelief="solid", bg='white', command=self.Exo_1)
        self.button1.place(x=150, y=175)

        self.button2 = Button(self.root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white', command=self.Exo_2)
        self.button2.place(x=370, y=175)


        self.root.mainloop()