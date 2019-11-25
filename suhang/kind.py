from tkinter import *

class Kind:
     def __init__(self):
        root = Tk()

        root.title("Dance_Kind")
        root.geometry("700x500+100+100")
        root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/kind.png")

        label = Label(root, text="이미지", image=image)
        label.pack()

        button1 = Button(root, width=15, height=8, text="K-pop", overrelief="solid", bg='salmon')
        button1.place(x=120, y=170)

        button2 = Button(root, width=15, height=8, text="Pop", overrelief="solid", bg='sandybrown')
        button2.place(x=290, y=170)

        button3 = Button(root, width=15, height=8, text="Girls Hiphop", overrelief="solid", bg='yellow')
        button3.place(x=460, y=170)

        button4 = Button(root, width=15, height=8, text="House", overrelief="solid", bg='lightgreen')
        button4.place(x=120, y=310)

        button5 = Button(root, width=15, height=8, text="Urban", overrelief="solid", bg='skyblue')
        button5.place(x=290, y=310)

        button6 = Button(root, width=15, height=8, text="B-boy", overrelief="solid", bg='palevioletred')
        button6.place(x=460, y=310)

        root.mainloop()