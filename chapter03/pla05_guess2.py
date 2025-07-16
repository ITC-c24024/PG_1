import random

ans=5
score=5
answer=random.randint(1,10)

while ans!=0:
    n=int(input("正解の数字は？"))
 
    if n==0:
        break
    elif n>answer:
        print("数字が大きいです")
        score-=1
    elif n<answer:
        print("数字が小さいです")
        score-=1
    else:
        print("当たりです！")
        print("数字変更")
        answer=random.randint(1,10)
        score+=10
        ans-=1

print("ゲーム終了")
print(f"持ち点:{score}")
