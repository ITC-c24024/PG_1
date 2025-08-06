change=int(input("お釣りを入力"))
print(f"お釣りの金額：{change}円")

_100=0
_10=0
_1=0

_100=change//100
change-=100*_100
_10=change//10
change-=10*_10
_1=change

print(f"100円玉{_100}枚,10円玉{_10}枚,1円玉{_1}枚")
