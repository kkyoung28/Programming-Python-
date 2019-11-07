#4-9
from tkinter import *
import webbrowser
from read_write import read


class Exo_1:
    def Link(self,num,final):
        link = ["https://youtu.be/7Zk5apxCYmI","https://youtu.be/_x6_pR--5Vs","https://youtu.be/yzPBBNowM4w","https://youtu.be/HKZ8p-NqWqE","https://youtu.be/P9tw9smiRBQ","https://youtu.be/Q2dAkDBMwV0"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self):
        self.root = Toplevel()

        self.root.title("엑소_공연영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/exo1.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="Monster", overrelief="solid", bg='salmon', command=lambda:self.Link(0, "Monster"))
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="전야", overrelief="solid", bg='sandybrown', command=lambda:self.Link(1, "전야"))
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="으르렁", overrelief="solid", bg='yellow', command=lambda:self.Link(2, "으르렁"))
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="Love me right", overrelief="solid", bg='lightgreen', command=lambda:self.Link(3, "Love me right"))
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="Call me baby", overrelief="solid", bg='skyblue', command=lambda:self.Link(4, "Call me baby"))
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="중독", overrelief="solid", bg='palevioletred', command=lambda:self.Link(5, "중독"))
        self.button6.place(x=460, y=310)

        self.root.mainloop()

