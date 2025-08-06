import random

class Vanpire():
    hour=14
    key=False
    have_map=False
    now="地上"
    pos=[0,0]

    rooms=[["0","0","0","k","m","d"],["0","0","0","0","♰","v"]]
    random.shuffle(rooms[0])
    random.shuffle(rooms[1])

    display=[[" "," "," "," "," "," "] for _ in range(2)]

    end=False

    def set_map(self):
        print("--------------------------")
        print(f"時刻：{self.hour}時\n現在地：{self.now}")
        print("カギ=k, 地図=m, 地下入口=d")
        if self.now=="地下":
            print("十字架=♰, 吸血鬼=v")
        print("--------------------------")
        print("♰ 吸血鬼の館 ♰")
        print(" 1 2 3 4 5 6")
        print("+-+-+-+-+-+-+")
        if self.have_map:
            for i in range(2):
                for n in range(6):
                    print(f"|{self.rooms[i][n]}",end="")
                print("|")
                print("+-+-+-+-+-+-+")
        else: 
            for i in range(6):
                print(f"|{self.display[0][i]}",end="")
            print("|")
            print("+-+-+-+-+-+-+")
            if self.now=="地下":
                for i in range(6):
                    print(f"|{self.display[1][i]}",end="")
                print("|")
                print("+-+-+-+-+-+-+")

    def move(self,n):
        self.hour+=1
        
        if self.now=="地上":
            s=self.rooms[0][n-1]
            self.display[0][n-1]=s
        else:
            s=self.rooms[1][n-1]
            self.display[1][n-1]=s

        if s=="0":
            print("何も見つかりませんでした\n")
        elif s=="k":
            print("カギを見つけました\n")
            self.key=True
        elif s=="m":
            print("地図を見つけました\n")
            self.have_map=True
        elif s=="d" and self.key==False:
            print("地下の入り口を見つけましたが入れません\n")
        elif s=="d" and self.key:
            print("地下のエリアに移動します\n")
            self.now="地下"
        elif s=="♰":
            print("十字架を見つけました\n")
        else:
            print("吸血鬼がいました！！\n")
            self.battle()
            return
        
        if self.hour==24:
            print("吸血鬼が目を覚ました…")
            self.battle()
            return

        self.set_map()

    def battle(self):
        input("Enter:吸血鬼と戦う")

        p=random.randint(1,7)
        if self.key:
            p+=3
        v=random.randint(1,7)
        
        if p>v:
            print("おめでとう！吸血鬼を倒すことができた！")
        elif p<v:
            print("残念！吸血鬼にやられてしまった…")
        else:
            print("""
そこには静粛があった。
立ち上がる者はなく、
ただひんやりとした空気だけがただよっていた。
あなたが吸血鬼を倒したのは事実だ。
だが、それを誰にも報告することはできない。
しばしの時を経て、誰かがあなたの偉業に気付く。
その時には、すでに吸血鬼の館はなく、
白い花が一輪咲いていた…
                  """)
        self.end=True

house=Vanpire()
print("===探索開始===")
house.set_map()

while house.end==False:
    i=int(input("どのエリアを探索しますか？"))
    house.move(i)
