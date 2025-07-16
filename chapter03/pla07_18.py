import random
hands = ["グー","チョキ","パー"]
p_score=0
c_score=0
p_finger=18
c_finger=18

#手に応じた指の消費量を計算
def fingerCheck(f):
    if f==0:
        f=0
    elif f==1:
        f=2
    else:
        f=5
    return f

#10回勝負
for n in range(0,10):
    print(f"{n+1}戦目")
    
    #選んだ手が出せるかを判定
    while True:
        i = random.randint(0,2)
        if c_finger>=fingerCheck(i):
            break
    while True:
        hand = hands.index(input("手を選んでください"))
        if p_finger<fingerCheck(hand):
            print("残りの指が足りません")
        else:
            break
    
    #結果を計算
    result = hand - i

    #結果に応じてスコア計算 
    if result == -1 or result == 2:
        print("プレイヤーの勝ち")
        if n==5 or n==9:
            p_score+=2
        else:
            p_score+=1
    elif result == 1 or result == -2:
        print("CPUの勝ち")
        if n==5 or n==9:
            c_score+=2
        else:
            c_score+=1
    else:
        print("あいこ")
    
    #指を消費
    c_finger-=fingerCheck(i)
    p_finger-=fingerCheck(hand)
    print(f"CPUの手{hands[i]},残りの指{c_finger},得点{c_score}")
    print(f"自分の手{hands[hand]},残りの指{p_finger},得点{p_score}")

#最終的なスコアを計算
p_score-=p_finger
c_score-=c_finger

#結果を表示
if p_score>c_score:
    print("プレイヤーの勝ち")
elif p_score<c_score:
    print("CPUの勝ち")
else:
    print("引き分け")
print(f"CPUの得点{c_score}:プレイヤーの得点{p_score}")
