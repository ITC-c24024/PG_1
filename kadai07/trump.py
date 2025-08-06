import random

class Card():
    marks=["ダイヤ","クローバー","スペード","ハート"]
    def __init__(self,mark,number):
        self.mark=self.marks[mark]
        self.number=number

trump=[Card(i,n) for i in range(0,4) for n in range(1,14)]
random.shuffle(trump)

print("あなたが引いたトランプは,")
for i in range(5):
    print(f"{trump[i].mark}の{trump[i].number}")
