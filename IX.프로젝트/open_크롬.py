import pyautogui as pag
import time

if __name__ == '__main__':
    #크롬 이미지 인식하자
    datas = pag.locateAllOnScreen("크롬아이콘.PNG")
    for data in datas:
        print(data)
        center=pag.center(data)
        pag.moveTo(center,duration=1)
    # print(data)
    # #가운데 좌표 찾자
    # center=pag.center(data)
    # #마우스 이동하자
    # # pag.moveTo(center,duration=2)
    # #더블클릭하자
    # pag.doubleClick(center, duration=2)