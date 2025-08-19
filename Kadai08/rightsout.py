field=[[" " for _ in range(5)] for _ in range(5)]
#2次元配列で管理することで、座標を用いてマスの位置指定が容易にできるようにしました。

def set_field():#盤面セット
    print("  1 2 3 4 5")
    for i in range(5):
        print(" -----------")
        print(i+1,end="")
        for n in range(5):
            print("|"+field[i][n],end="")
        print("|")
    print(" -----------")
set_field()

def change_status(x,y):#マスの状態切り替え
    if field[y-1][x-1]==" ":
        field[y-1][x-1]="0"
    else:
        field[y-1][x-1]=f" "

def check_field():#すべて埋まっているかチェック
    for i in range(5):
        for n in range(5):
            if field[i][n]==" ":
                return False
    return True
    #boolが返ってくるようにすることで、ループから抜ける判断をしやすくしました。

print("すべてのマスを0にしてください")
while True:
    x,y=map(int,input("マスを選んでください 入力例(1 3)：").split())
    
    change_status(y,x)

    #for文一つで簡潔に四方の位置を確認できるようにしました。
    for i in range(-1,2):
        if 0<y+i<6 and i!=0:
            change_status(y+i,x)
        if 0<x+i<6 and i!=0:
            change_status(y,x+i)
    
    set_field()

    if check_field():
        break

print("ゲームクリア")
