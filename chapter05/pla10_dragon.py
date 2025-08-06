import random

print("""
      """)
full=10
mood=10
dec=1
action=[0]*4
input_list=[]
day=["朝","昼","夕方","夜"]
unnti=False
print('''
                                 _/|__
             _,-------,        _/ -|  \_     /~>.
          _-~ __--~~/\ |      (  \   /  )   | / |
       _-~__--    //   \\      \ *   * /   / | ||
    _-~_--       //     ||      \     /   | /  /|
   ~ ~~~~-_     //       \\     |( " )|  / | || /
           \   //         ||    | VWV | | /  ///
     |\     | //           \\ _/      |/ | ./|
     | |    |// __         _-~         \// |  /
    /  /   //_-~  ~~--_ _-~  /          |\// /
   |  |   /-~        _-~    (     /   |/ / / 
  /   /           _-~  __    |   |____|/     
 |   |__         / _-~  ~-_  (_______  `\    
 |      ~~--__--~ /  _     \        __\)))  
  \               _-~       |     ./  \      
   ~~--__        /         /    _/     |     
         ~~--___/       _-_____/      /      
          _____/     _-_____/      _-~       
       /^<  ___       -____         -____ 
          ~~   ~~--__      ``\--__       ``\   
                     ~~--\)\)\)   ~~--\)\)\) 
      ''')
name=input("ドラゴンに名前を付けてください")

# お世話
def meal():
    global full
    full+=2
    if full>10:
        full=10

    i=random.randint(0,2)
    match i:
        case 0:
            print(f"{name}は美味しそうに食べた")
        case 1:
            print(f"{name}は嫌そうに食べた")
def cleaning():
    global full
    full-=1
    if full>10:
        full=10
    global dec
    dec=3
    unnti=False

    i=random.randint(0,2)
    match i:
        case 0:
            print(f"{name}は家が綺麗になって喜んだ")
        case 1:
            print(f"{name}は機嫌を直した")
def walk():
    global full
    full-=1
    if full>10:
        full=10
    global mood
    mood+=1
    if mood>10:
        mood=10

    i=random.randint(0,2)
    match i:
        case 0:
            print(f"{name}は歩き疲れた")
        case 1:
            print(f"{name}はうんこを踏んだ")
def sleep():
    global full
    full-=2
    if full>10:
        full=10
    global mood
    mood+=2
    if mood>10:
        mood=10

    i=random.randint(0,2)
    match i:
        case 0:
            print(f"{name}はすぐに眠った")
        case 1:
            print(f"{name}は渋々眠った")

# 7日繰り返す
for i in range(0,7):
    print(f"\n==={i+1}日目===")
    print(f"{name}がうんちをしました。掃除をしましょう。")
    unnti=True
    dec+=3
    # 1日4回行動
    for n in range(0,4):
        print(f"\n{day[n]}のお世話をしよう")
        print(f"満腹度:{full},機嫌度:{mood}",end=" ")
        print("💩"*(dec//3))

        if action.count(1)<3:
            input_list.append(1)
            print("1:食事(満腹度＋２)")
        if action[n-1]!=2:
            input_list.append(2)
            print("2:掃除(満腹度－１、機嫌度の減少を１に戻します)")
        if action[n-1]!=3:
            input_list.append(3)
            print("3:散歩(満腹度－１、機嫌度＋１)")
        input_list.append(4)
        print("4:睡眠(満腹度－２、機嫌度＋２)")
        print("数字を入力してください")
        # 入力チェック
        while True:
            try:
                act=int(input())
            except ValueError:
                print("＊数字を入力してください")
            else:
                if act in input_list:
                    break
                else:
                    print("＊選択肢から選んでください")
        input_list.clear()

        # お世話
        match act:
            case 1:
                meal()
            case 2:
                cleaning()
            case 3:
                walk()
            case 4:
                sleep()

        # 行動を記録
        action[n]=act

        # ゲーム終了
        if full<=0 or mood<=0:
            break

    # 行動を振り返る
    if 1 not in action: # 食事を与えなかった
        full-=3
    if 4 not in action: # 睡眠を与えなかった
        mood-=dec
    action.clear()
    action=[0]*4

    # ゲーム終了
    if full<=0:
        print("\n===ゲームオーバー===")
        print(f"あなたは{name}の胃袋に入ってしまった")
        break
    if mood<=0:
        print("\n===ゲームオーバー===")
        print(f"{name}はあなたと同じ世界に住みたくなかった")
        break
    if i==6:
        print("\n===ゲームクリア===")
print('''
 ___________________________________________________
 @@@@@@@@@@@@@@@@@@@@@**^^""~~~"^@@^*@*@@**@@@@@@@@@
 @@@@@@@@@@@@@*^^'"~   , - ' '; ,@@b. '  -e@@@@@@@@@
 @@@@@@@@*^"~      . '     . ' ,@@@@(  e@*@@@@@@@@@@
 @@@@@^~         .       .   ' @@@@@@, ~^@@@@@@@@@@@
 @@@~ ,e**@@*e,  ,e**e, .    ' '@@@@@@e,  "*@@@@@'^@
 @',e@@@@@@@@@@ e@@@@@@       ' '*@@@@@@    @@@'   0
 @@@@@@@@@@@@@@@@@@@@@',e,     ;  ~^*^'    ;^~   ' 0
 @@@@@@@@@@@@@@@^""^@@e@@@   .'           ,'   .'  @
 @@@@@@@@@@@@@@'    '@@@@@ '         ,  ,e'  .    ;@
 @@@@@@@@@@@@@' ,&&,  ^@*'     ,  .  i^"@e, ,e@e  @@
 @@@@@@@@@@@@' ,@@@@,          ;  ,& !,,@@@e@@@@ e@@
 @@@@@,~*@@*' ,@@@@@@e,   ',   e^~^@,   ~'@@@@@@,@@@
 @@@@@@, ~" ,e@@@@@@@@@*e*@*  ,@e  @@""@e,,@@@@@@@@@
 @@@@@@@@ee@@@@@@@@@@@@@@@" ,e@' ,e@' e@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@" ,@" ,e@@e,,@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@~ ,@@@,,0@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@@@@@@@@@@,,@@@@@@@@@@@@@@@@@@@@@@@@@
 """""""""""""""""""""""""""""""""""""""""""""""""""
 
''')
