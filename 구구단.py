dan = 2
# print(dan,"x", 1, "=", dan*1)
# print(dan,"x", 2, "=", dan*2)
# print(dan,"x", 3, "=", dan*3)
# print(dan,"x", 4, "=", dan*4)
# print(dan,"x", 5, "=", dan*5)
# print(dan,"x", 6, "=", dan*6)
# print(dan,"x", 7, "=", dan*7)
# print(dan,"x", 8, "=", dan*8)
# print(dan,"x", 9, "=", dan*9)
for dan in range(2, 9+1):
    for i in range(1, 9+1):
        if i > 7:
            break
        if i % 2 == 0:
            continue
        print(dan, "x", i, "=", dan*i)
    print("----------------------")