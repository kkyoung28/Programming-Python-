from tkinter import *
from seven_1 import Seven_1
from seven_2 import Seven_2

class Video_seven:
    def Seven_1(self):
        seven_1 = Seven_1()
        print("세븐틴 공연영상입니다 !")
        open(file="seven_1.py")

    def Seven_2(self):
        seven_2 = Seven_2()
        print("세븐틴 정식촬영영상입니다 !")
        open(file="seven_2.py")

    def __init__(self):

        self.root = Toplevel()

        self.root.title("Kind_Video")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/videokind.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=25, height=15, text="공연영상", overrelief="solid", bg='white', command=self.Seven_1)
        self.button1.place(x=150, y=175)

        self.button2 = Button(self.root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white', command=self.Seven_2)
        self.button2.place(x=370, y=175)


        self.root.mainloop()