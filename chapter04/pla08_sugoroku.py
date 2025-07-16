import random

map_s=["[]"]*30
shuffle=[0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5]
event=[]
for i in range(0,len(map_s)):
    n=random.randint(0,len(shuffle)-1)
    e=shuffle.pop(n)
    event.append(e)
turn=0
place=[0,0]
money=[5,5]
skip=[False,False]

def set_map():
    print("[S]",end="")
    for i in range(0,len(map_s)-1):
        print(map_s[i],end="")
    print("[G]\n")
    
    if turn==0:
        print("playerのターン")
    else:
        print("comのターン")

def input_check():
    while True:
        k=input("sを入力してサイコロ振る")
        if k=="s":
            return True 

def move(x):
    # マスの状態を更新
    ## 前回のマスから自分を除く
    if map_s[place[turn]-1]=="[p c]":
        if turn==0:
            map_s[place[turn]-1]="[c]"
        else:
            map_s[place[turn]-1]="[p]"
    else:
        map_s[place[turn]-1]="[]"

    place[turn]+=x

    ## ゴールを超える場合超える分戻る
    if place[turn]>30:
        over=place[turn]-30
        place[turn]=30-over

    ## 移動したマスに自分を置く
    if place[0]==place[1]:
        map_s[place[turn]-1]="[p c]"
    elif turn==0:
        map_s[place[turn]-1]="[p]"
    else:
        map_s[place[turn]-1]="[c]"

# イベント関数
def get_money():
    m=random.randint(1,3)
    money[turn]+=m
    print(f"金貨を{m}枚ゲット")
def loss_money():
    m=random.randint(1,3)
    money[turn]-=m
    print(f"金貨を{m}枚ロス")
def go():
    x=random.randint(1,3)
    move(x)
    print(f"{x}マス進む")
def back():
    x=random.randint(1,3)
    move(-x)
    print(f"{x}マス戻る")
def stay():
    print("1回休み")
    skip[turn]=True
def restart():
    move(-place[turn])
    print("振り出しに戻る")

print("=====ゲームスタート=====")
set_map()
while True:
    # 出目を決める
    if input_check():
        num=random.randint(1,6)
        print(f"出目:{num}")
    move(num)
    
    if place[turn]==30:
        break
    
    match event[place[turn]-1]:
        case 0:
            get_money()  
        case 1:
            loss_money()
        case 2:
            go()
        case 3:
            back()
        case 4:
            stay()
        case 5:
            restart()
    
    print(f"金貨:{money[turn]}枚")

    if place[turn]==30:
        break

    if skip[1-turn]==False:
        turn=1-turn
    else:
        skip[1-turn]=False

    set_map()

print("\n=====ゲーム終了=====")
if turn==0:
    print("スピード的勝利:player")
else:
    print("スピード的勝利:com")
if money[0]>money[1]:
    print("金銭的勝利:player")
elif money[0]<money[1]:
    print("金銭的勝利:player")
else:
    print("金銭的勝利:なし")
print(f"金貨:player{money[0]}枚,com{money[1]}枚")
