import pyautogui as pag
import time

if __name__ == '__main__':
    pag.moveTo(73, 1057, 2)
    pag.click()
    pag.moveTo(439,543, 2)
    pag.click()
    pag.moveTo(24, 69, 2)
    pag.click()
    pag.typewrite("Hello world")
    pag.press("enter")
    pag.press("enter")
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    pag.hotkey('ctrl', 's')
    pag.moveTo(170, 488)
    pag.doubleClick()
    # pag.typewrite("C:\\Users\\kjhh9\\Downloads")
    pag.typewrite("vkdlTjs dnjfem", interval=0.5)
    pag.moveTo(805, 564, 2)
    pag.click()


    #메모장 프로그램 실행하자
    #hello world 치자
    #두번 내리자
    #반갑구나 세상아 치자
    #저장하자
    #파일이름: 파이썬월드