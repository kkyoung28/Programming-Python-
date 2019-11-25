from tkinter import *
# class Kind:
#     def __init__(self):
root = Tk()

root.title("Kind_Video")
root.geometry("700x500+100+100")
root.resizable(False, False)

        # 레이블 생성, 메인이미지 삽입
image = PhotoImage(file="img/videokind.png")

label = Label(root, text="이미지", image=image)
label.pack()

button1 = Button(root, width=25, height=15, text="공연영상", overrelief="solid", bg='white')
button1.place(x=150, y=175)

button2 = Button(root, width=25, height=15, text="공식촬영영상", overrelief="solid", bg='white')
button2.place(x=370, y=175)


root.mainloop()