#4-7
from tkinter import *
import webbrowser
from read_write import read


class Bts_1:
    def Link(self,num,final):
        link = ["https://youtu.be/WmGT7HoUqi0","https://youtu.be/H5dd2x8MV2o","https://youtu.be/BloMUUgaQXo","https://youtu.be/oFuY5M1lwiY","https://youtu.be/1dxnzJEusc4","https://youtu.be/CGuShacPoJ8"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self):
        self.root = Toplevel()

        self.root.title("방탄소년단_공연영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/bts1.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="I NEED U", overrelief="solid", bg='salmon', command=lambda:self.Link(0, "I NEED U"))
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="Mic drop", overrelief="solid", bg='sandybrown', command=lambda:self.Link(1, "Mic drop"))
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="Fake love", overrelief="solid", bg='yellow', command=lambda:self.Link(2, "Fake love"))
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="작은 것들을 위한 시", overrelief="solid", bg='lightgreen', command=lambda:self.Link(3, "작은 것들을 위한 시"))
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="피 땀 눈물", overrelief="solid", bg='skyblue', command=lambda:self.Link(4, "피 땀 눈물"))
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="IDOL", overrelief="solid", bg='palevioletred', command=lambda:self.Link(5, "IDOL"))
        self.button6.place(x=460, y=310)

        self.root.mainloop()

