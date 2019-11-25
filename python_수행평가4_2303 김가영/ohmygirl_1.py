#4-1
from tkinter import *
import webbrowser
from read_write import read


class OhmyGirl_1:
    def Link(self,num,final): #버튼 마다 링크 연결
        link = ["https://youtu.be/iR4c4T5XlVU","https://youtu.be/Vn2411mYUFE","https://youtu.be/X72HgBrMccc","https://youtu.be/BrASylNQj8c","https://youtu.be/vnXwAJDxtKo","https://youtu.be/AOcX6lcLYvk"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self): #창 생성
        self.root = Toplevel()

        self.root.title("오마이걸_공연영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/oh1.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="CLOSER", overrelief="solid", bg='salmon', command=lambda:self.Link(0,"CLOSER"))
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="한 발짝 두 발짝", overrelief="solid", bg='sandybrown', command=lambda:self.Link(1,"한 발짝 두 발짝"))
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="다섯 번째 계절", overrelief="solid", bg='yellow', command=lambda:self.Link(2,"다섯 번째 계절"))
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="불꽃놀이", overrelief="solid", bg='lightgreen', command=lambda:self.Link(3,"불꽃놀이"))
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="BUNGEE", overrelief="solid", bg='skyblue', command=lambda:self.Link(4,"BUNGEE"))
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="LIAR LIAR", overrelief="solid", bg='palevioletred', command=lambda:self.Link(5,"LIAR LIAR"))
        self.button6.place(x=460, y=310)

        self.root.mainloop()

