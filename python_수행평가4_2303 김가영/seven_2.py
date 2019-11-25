#4-11
from tkinter import *
import webbrowser
from read_write import read


class Seven_2:
    def Link(self,num,final): #버튼 마다 링크 연결
        link = ["https://youtu.be/oBM37bYX4dU","https://youtu.be/5HeKFck9SWY","https://youtu.be/wH5xX2hH6xA","https://youtu.be/IkByqFNzQAU","https://youtu.be/6Ie9llP16og","https://youtu.be/gzkS2oX1RF8"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self): #창 생성
        self.root = Toplevel()

        self.root.title("세븐틴_공식촬영영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/seven2.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="Fear(독)", overrelief="solid", bg='salmon', command=lambda:self.Link(0, "Fear(독)"))
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="Home", overrelief="solid", bg='sandybrown', command=lambda:self.Link(1, "Home"))
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="박수", overrelief="solid", bg='yellow', command=lambda:self.Link(2, "박수"))
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="울고싶지않아", overrelief="solid", bg='lightgreen', command=lambda:self.Link(3, "울고싶지않아"))
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="고맙다", overrelief="solid", bg='skyblue', command=lambda:self.Link(4, "고맙다"))
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="만세", overrelief="solid", bg='palevioletred', command=lambda:self.Link(5, "만세"))
        self.button6.place(x=460, y=310)

        self.root.mainloop()

