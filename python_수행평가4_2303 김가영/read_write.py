#마지막으로 누른 버튼 이름 기록한 파일 읽어오는 함수
class read:
    def __init__(self,final):
        f =open("final.txt","w",encoding="UTF-8")
        f.write(final)