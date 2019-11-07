from tkinter import *
from ohmygirl_1 import OhmyGirl_1
from ohmygirl_2 import OhmyGirl_2

class Video_oh:
    def OhmyGirl_1(self):
        ohmygirl_1 = OhmyGirl_1()
        print("오마이걸 공연영상입니다 !")
        open(file="ohmygirl_1.py")
        
    def OhmyGirl_2(self):
        ohmygirl_2 = OhmyGirl_2()
        print("오마이걸 정식촬영영상입니다 !")
        open(file="ohmygirl_2.py")
        
    def __init__(self):

        self.root = Toplevel()

        self.root.title("Kind_Video")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/videokind.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=25, height=15, text="공연영상", overrelief="solid", bg='white', command=self.OhmyGirl_1)
        self.button1.place(x=150, y=175)

        self.button2 = Button(self.root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white', command=self.OhmyGirl_2)
        self.button2.place(x=370, y=175)


        self.root.mainloop()