#2303 김가영
#여러 장르의 춤(노래, 영상)을 모아둔 프로그램
#실행 main.py에서 하시면 됩니다!

from tkinter import *
from kind import Kind
# import kind



# class main:
#     def __init__(self):
#         self.dk = DanceKind()

#창 생성
root = Tk()

root.title("You Dance?")
root.geometry("700x500+100+100")
root.resizable(False,False)

#레이블 생성, 메인이미지 삽입
image = PhotoImage(file="img/main.png")

label=Label(root, text="이미지", image=image)
label.pack()

#메뉴버튼 춤 장르만 활성화 나머지는 아직 X
def kind():
    kind=Kind()
    print("원하는 춤 장르를 선택하세요!")
    open(file="kind.py")

button1 = Button(root, width=15, height=10, text="춤 장르", overrelief="solid", bg='white', command=kind)
button1.place(x=70, y=240)

button2 = Button(root, width=15, height=10, text="연습실", overrelief="solid", bg='gray')
button2.place(x=220, y=240)

button3 = Button(root, width=15, height=10, text="요즘 유행하는 춤", overrelief="solid", bg='gray')
button3.place(x=370, y=240)

button4 = Button(root, width=15, height=10, text="요즘 유행하는 노래", overrelief="solid", bg='gray')
button4.place(x=520, y=240)



root.mainloop()