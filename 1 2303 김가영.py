#학번을 입력받고, 학년 학과 반 번호를 출력하자

student=(input())

grade=student[0]
classroom=student[1]
num=student[2:4]

if grade == "1" or grade == "2":
    if classroom == "1" or classroom == "2":     
         print(grade+"학년","뉴미디어소프트웨어과",classroom+"반",num+"번")
    elif classroom == "3" or classroom == "4":
         print(grade+"학년","뉴미디어웹솔루션과",classroom+"반",num+"번")
    elif classroom == "5" or classroom == "6":
         print(grade+"학년","뉴미디어디자인과",classroom+"반",num+"번")
elif grade == "3":
    if classroom == "1" or classroom == "2":
         print(grade+"학년","인터랙티브미디어과",classroom+"반",num+"번")
    elif classroom == "3" or classroom == "4":
         print(grade+"학년","뉴미디어디자인과",classroom+"반",num+"번")
    elif classroom == "5" or classroom == "6":
         print(grade+"학년","뉴미디어솔루션과",classroom+"반",num+"번")