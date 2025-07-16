import random
hands = ["グー","チョキ","パー"]
pr=0
cpur=0

for n in range(0,10):
    i = random.randint(0,2)
    hand = hands.index(input("手を選んでください"))
    result = hand - i

    print(f"CPUの手{hands[i]}")
    print(f"自分の手{hands[hand]}")

    if result == -1 or result == 2:
        print("プレイヤーの勝ち")
        pr+=1
    elif result == 1 or result == -2:
        print("CPUの勝ち")
        cpur+=1
    else:
        print("あいこ")

print(f"{pr}:{cpur}")
if pr>cpur:
    print("プレイヤーの勝ち")
elif pr<cpur:
    print("CPUの勝ち")
else:
    print("引き分け")
