#2303 김가영
#여러 장르의 춤(노래, 영상)을 모아둔 프로그램
#종료하려고 할 때 오늘 봤던 것들 기록이 뜸
#실행 main.py에서 하시면 됩니다! 끄는 것도 main.py 끄시면 됩니다!
#1

from tkinter import *
from kind import Kind
from tkinter import messagebox as msg

#창 생성
root = Tk()

root.title("You Dance?")
root.geometry("700x500+100+100")
root.resizable(False,False)

#레이블 생성, 메인이미지 삽입
image = PhotoImage(file="img/main.png")

label=Label(root, text="이미지", image=image)
label.pack()

# 준비중 메세지 박스 띄우는 함수
def fbutton1():
    msg.showwarning('연습실', '아직 준비중입니다!')

def fbutton2():
    msg.showwarning('요즘 유행하는 춤', '아직 준비중입니다!')

def fbutton3():
    msg.showwarning('요즘 유행하는 노래', '아직 준비중입니다!')

#메뉴버튼 춤 장르만 활성화 나머지는 아직 X
#춤 장르 버튼 클릭시 kind.py로 이동할 수 있는 함수
def kind():
    kind=Kind()
    print("원하는 춤 장르를 선택하세요!")
    open(file="kind.py")

button1 = Button(root, width=15, height=10, text="춤 장르", overrelief="solid", bg='white', command=kind)
button1.place(x=70, y=240)

button2 = Button(root, width=15, height=10, text="연습실", overrelief="solid", bg='gray', command=fbutton1)
button2.place(x=220, y=240)

button3 = Button(root, width=15, height=10, text="요즘 유행하는 춤", overrelief="solid", bg='gray', command=fbutton2)
button3.place(x=370, y=240)

button4 = Button(root, width=15, height=10, text="요즘 유행하는 노래", overrelief="solid", bg='gray', command=fbutton3)
button4.place(x=520, y=240)

#종료버튼(X) 클릭 시 나오는 메세지 창 함수
def on_closing():
    if msg.askokcancel("종료", "종료하시겠습니까?"):
        f = open("final.txt", "r", encoding="utf8")  
        text = f.read()
        msg.showinfo("마지막으로 선택된 버튼", text) #마지막으로 선택된 버튼 파일을 불러오고 메세지 창으로 띄움
        print(text)
        f.close()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
