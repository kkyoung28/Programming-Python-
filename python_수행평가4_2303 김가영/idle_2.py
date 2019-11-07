#4-4
from tkinter import *
import webbrowser
from read_write import read


class Idle_2:
    def Link(self,num,final):
        link = ["https://youtu.be/vUos4Qaxu08","https://youtu.be/FogX5i9JO4w","https://youtu.be/fgD_o3nwsGI","https://youtu.be/EY2JikssROI"]
        webbrowser.open(link[num])
        read(final)

    def __init__(self):
        self.root = Toplevel()

        self.root.title("(여자)아이들_공식촬영영상")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        imagekind = PhotoImage(file="img/idle2.png")

        label1 = Label(self.root, text="이미지", image=imagekind)
        label1.pack()

        self.button1 = Button(self.root, width=15, height=10, text="LATATA", overrelief="solid", bg='white', command=lambda:self.Link(0, "LATATA"))
        self.button1.place(x=70, y=240)

        self.button2 = Button(self.root, width=15, height=10, text="HANN", overrelief="solid", bg='white', command=lambda:self.Link(1, "HANN"))
        self.button2.place(x=220, y=240)

        self.button3 = Button(self.root, width=15, height=10, text="senorita", overrelief="solid", bg='white', command=lambda:self.Link(2, "Senorita"))
        self.button3.place(x=370, y=240)

        self.button4 = Button(self.root, width=15, height=10, text="Uh-oh", overrelief="solid", bg='white', command=lambda:self.Link(3, "Uh-oh"))
        self.button4.place(x=520, y=240)

        self.root.mainloop()

