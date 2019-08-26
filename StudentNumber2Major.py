#학번입력받아
#학과 출력하기
#예: "2320"을 입력하면, "뉴미디어웹솔루션과"를 출력

# print("학번을 입력하셈")
# num=(input())

# if num[0:3] == 11 or 12 or 21 or 22 :
#     print("뉴미디어소프트웨어과")

# elif num[0:3] == 13 or 14 or 23 or 24 :
#     print("뉴미디어웹솔루션과")

# elif num[0:3] == 15 or 16 or 25 or 26 or 34 or 35 :
#     print("뉴미디어디자인과")

# elif num[0:3] == 31 or 32 :
#     print("인터랙티브미디어과")

# elif num[0:3] == 35 or 36 :
#     print("뉴미디어솔루션과")


majors = [["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
["뉴미디어소프트웨어과","뉴미디어웹솔루션과","뉴미디어디자인과"],
["인터랙티브미디어과","뉴미디어디자인과","뉴미디어솔루션과"]]
#start
student_number=input("학번을 입력하세야 :")

grade = student_number[0]
grade = int(grade)
classroom = student_number[1]
classroom = int(classroom)
print(majors[grade-1][(classroom-1)//2])
#end



# if grade == "1" or grade == "2":
#     print(majors12학년[classroom-1])
# elif grade == 3:
#     print(majors3학년[classroom-1])

#     if classroom == "1" or classroom == "2":
#         print("뉴미디어소프트웨어과")
#     elif classroom == "3" or classroom == "4":
#         print("뉴미디어웹솔루션과")
#     elif classroom == "5" or classroom == "6":
#         print("뉴미디어디자인과")
# elif grade == "3":
#     if classroom == "1" or classroom == "2":
#         print("인터랙티브미디어과")
#     elif classroom == "3" or classroom == "4":
#         print("뉴미디어디자인과")
#     elif classroom == "5" or classroom == "6":
#         print("뉴미디어솔루션과")