import random

answer=random.randint(1,10)

for i in range(0,10):
    n=int(input("正解の数字は？"))
    if n>answer:
        print("数字が大きいです")
    elif n<answer:
        print("数字が小さいです")
    else:
        print("当たりです！")
        break
    if i==9:
        print("残念です！")
