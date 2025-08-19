import random

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

#ドラゴンの情報、お世話をクラスにまとめました。
class Dragon():
    name=""
    full=10
    mood=10
    dec=1
    action=[0]*4
    input_li=[]
    day=["朝","昼","夕方","夜"]
    unnti=False
    
    def __init__(self,name):
        self.name=name

    # お世話
    def meal(self):
        self.full
        self.full+=2
        if self.full>10:
            self.full=10

        i=random.randint(0,2)
        match i:
            case 0:
                print(f"{name}は美味しそうに食べた")
            case 1:
                print(f"{name}は嫌そうに食べた")
    
    def cleaning(self):
        self.full
        self.full-=1
        if self.full>10:
            self.full=10
        
        self.dec
        self.dec=3

        self.unnti=False

        i=random.randint(0,2)
        match i:
            case 0:
                print(f"{name}は家が綺麗になって喜んだ")
            case 1:
                print(f"{name}は機嫌を直した")

    def walk(self):
        self.full
        self.full-=1
        if self.full>10:
            self.full=10

        self.mood
        self.mood+=1
        if self.mood>10:
            self.mood=10

        i=random.randint(0,2)
        match i:
            case 0:
                print(f"{name}は歩き疲れた")
            case 1:
                print(f"{name}はうんこを踏んだ")

    def sleep(self):
        self.full
        self.full-=2
        if self.full>10:
            self.full=10
        
        self.mood
        self.mood+=2
        if self.mood>10:
            self.mood=10

        i=random.randint(0,2)
        match i:
            case 0:
                print(f"{name}はすぐに眠った")
            case 1:
                print(f"{name}は渋々眠った")

    #取った行動によって可能な選択肢のみ表示しました。。
    def act_select(self):
        print(f"\n{self.day[n]}のお世話をしよう")
        print(f"満腹度:{self.full},機嫌度:{self.mood}",end=" ")
        print("💩"*(self.dec//3))

        if self.action.count(1)<3:
            self.input_li.append(1)
            print("1:食事(満腹度＋２)")
        if self.action[n-1]!=2:
            self.input_li.append(2)
            print("2:掃除(満腹度－１、機嫌度の減少を１に戻します)")
        if self.action[n-1]!=3:
            self.input_li.append(3)
            print("3:散歩(満腹度－１、機嫌度＋１)")
        self.input_li.append(4)
        print("4:睡眠(満腹度－２、機嫌度＋２)")
        print("数字を入力してください")

    def act_check(self):
        # 行動を振り返る
        if 1 not in self.action: # 食事を与えなかった
            self.full-=3
        if 4 not in self.action: # 睡眠を与えなかった
            self.mood-=self.dec
        self.action.clear()
        self.action=[0]*4

name=input("ドラゴンに名前を付けてください")
dragon=Dragon(name)

# 7日繰り返す
for i in range(0,7):
    print(f"\n==={i+1}日目===")
    print(f"{dragon.name}がうんちをしました。掃除をしましょう。")
    dragon.unnti=True
    dragon.dec+=3
    # 1日4回行動
    for n in range(0,4):
        dragon.act_select()

        # 入力チェック
        #正しい入力だけ受け付けるようにしました。
        while True:
            try:
                act=int(input())
            except ValueError:
                print("＊数字を入力してください")
            else:
                if act in dragon.input_li:
                    break
                else:
                    print("＊選択肢から選んでください")
        dragon.input_li.clear()

        # お世話
        match act:
            case 1:
                dragon.meal()
            case 2:
                dragon.cleaning()
            case 3:
                dragon.walk()
            case 4:
                dragon.sleep()

        # 行動を記録
        #行動をリストで記録し、選択肢や行動を振り返りやすくしました。
        dragon.action[n]=act

        # ゲーム終了
        if dragon.full<=0 or dragon.mood<=0:
            break

    dragon.act_check()

    # ゲーム終了
    if dragon.full<=0:
        print("\n===ゲームオーバー===")
        print(f"あなたは{dragon.name}の胃袋に入ってしまった")
        break
    if dragon.mood<=0:
        print("\n===ゲームオーバー===")
        print(f"{dragon.name}はあなたと同じ世界に住みたくなかった")
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
