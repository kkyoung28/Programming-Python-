#4-6
from tkinter import *
import webbrowser
from read_write import read


class Love_2:
    def Link(self,num,final): #버튼 마다 링크 연결
        link = ["https://youtu.be/xGVNmYgpK7U","https://youtu.be/VqJGeBzTqtE","https://youtu.be/cz9YCcCjXNI","https://youtu.be/yenrsHuUmeo","https://youtu.be/FQUfHP-tQ8s","https://youtu.be/3Dl9vuWHzto"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self): #창 생성
        self.root = Toplevel()

        self.root.title("러블리즈_공식촬영영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/love2.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()



        self.button1 = Button(self.root, width=15, height=8, text="안녕(Hi~)", overrelief="solid", bg='salmon', command=lambda:self.Link(0, "안녕(Hi~)"))
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="Ah-choo", overrelief="solid", bg='sandybrown', command=lambda:self.Link(1, "Ah-choo"))
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="그날의 너", overrelief="solid", bg='yellow', command=lambda:self.Link(2, "그날의 너"))
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="Candy Jelly Love", overrelief="solid", bg='lightgreen', command=lambda:self.Link(3, "Candy Jelly Love"))
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="Destiny(나의지구)", overrelief="solid", bg='skyblue', command=lambda:self.Link(4, "Destiny(나의지구)"))
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="그 시절 우리가 사랑했던 우리", overrelief="solid", bg='palevioletred', command=lambda:self.Link(5, "그 시절 우리가 사랑했던 우리"))
        self.button6.place(x=460, y=310)

        self.root.mainloop()

