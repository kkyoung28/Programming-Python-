f = open("file.txt","r", encoding="utf8") #r: read text
text = f.read()
print(text)
f.close()

#한줄씩 읽어오자
f = open("file.txt","r", encoding="utf8") #r: read text

text0 = f.readline()    #\n 까지 읽기
print(text0)            #\n
text1 = f.readline()
print(text1)

f.close()