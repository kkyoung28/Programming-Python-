#3
from tkinter import *
from video_oh import Video_oh
from video_idle import Video_idle
from video_love import Video_love
from video_bts import Video_bts
from video_exo import Video_exo
from video_seven import Video_seven

class Kpop:
      def Video_oh(self):
         video_oh = Video_oh()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_oh.py")

      def Video_idle(self):
         video_idle = Video_idle()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_idle.py")

      def Video_love(self):
         video_love = Video_love()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_love.py")

      def Video_bts(self):
         video_bts = Video_bts()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_bts.py")

      def Video_exo(self):
         video_exo = Video_exo()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_exo.py")

      def Video_seven(self):
         video_seven = Video_seven()
         print("원하는 영상종류를 선택하세요!")
         open(file="video_seven.py")

      def __init__(self):
        self.root = Toplevel()

        self.root.title("Kind_K-pop")
        self.root.geometry("700x500+100+100")
        self.root.resizable(False, False)

                # 레이블 생성, 메인이미지 삽입
        image = PhotoImage(file="img/kpop.png")

        label = Label(self.root, text="이미지", image=image)
        label.pack()

        self.button1 = Button(self.root, width=15, height=8, text="오마이걸", overrelief="solid", bg='pink', command=self.Video_oh)
        self.button1.place(x=120, y=170)

        self.button2 = Button(self.root, width=15, height=8, text="(여자)아이들", overrelief="solid", bg='pink', command=self.Video_idle)
        self.button2.place(x=290, y=170)

        self.button3 = Button(self.root, width=15, height=8, text="러블리즈", overrelief="solid", bg='pink', command=self.Video_love)
        self.button3.place(x=460, y=170)

        self.button4 = Button(self.root, width=15, height=8, text="방탄소년단", overrelief="solid", bg='skyblue', command=self.Video_bts)
        self.button4.place(x=120, y=310)

        self.button5 = Button(self.root, width=15, height=8, text="엑소", overrelief="solid", bg='skyblue', command=self.Video_exo)
        self.button5.place(x=290, y=310)

        self.button6 = Button(self.root, width=15, height=8, text="세븐틴", overrelief="solid", bg='skyblue', command=self.Video_seven)
        self.button6.place(x=460, y=310)

        self.root.mainloop()