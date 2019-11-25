from tkinter import *
# class Kind:
#     def __init__(self):
root = Tk()

root.title("Kind_K-pop")
root.geometry("700x500+100+100")
root.resizable(False, False)

        # 레이블 생성, 메인이미지 삽입
image = PhotoImage(file="img/kpop.png")

label = Label(root, text="이미지", image=image)
label.pack()

button1 = Button(root, width=15, height=8, text="오마이걸", overrelief="solid", bg='pink')
button1.place(x=120, y=170)

button2 = Button(root, width=15, height=8, text="(여자)아이들", overrelief="solid", bg='pink')
button2.place(x=290, y=170)

button3 = Button(root, width=15, height=8, text="러블리즈", overrelief="solid", bg='pink')
button3.place(x=460, y=170)

button4 = Button(root, width=15, height=8, text="방탄소년단", overrelief="solid", bg='skyblue')
button4.place(x=120, y=310)

button5 = Button(root, width=15, height=8, text="엑소", overrelief="solid", bg='skyblue')
button5.place(x=290, y=310)

button6 = Button(root, width=15, height=8, text="세븐틴", overrelief="solid", bg='skyblue')
button6.place(x=460, y=310)

root.mainloop()