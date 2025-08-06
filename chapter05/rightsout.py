field=[[" " for i in range(5)] for n in range(5)]

def set_field():
    print("  1 2 3 4 5")
    for i in range(5):
        print(" -----------")
        print(i+1,end="")
        for n in range(5):
            print("|"+field[i][n],end="")
        print("|")
    print(" -----------")
set_field()

def change_status(x,y):
    if field[y-1][x-1]==" ":
        field[y-1][x-1]="0"
    else:
        field[y-1][x-1]=f" "

def check_field():
    for i in range(5):
        for n in range(5):
            if field[i][n]==" ":
                return False
    return True        

print("すべてのマスを0にしてください")
while True:
    x,y=map(int,input("マスを選んでください").split())
    
    change_status(y,x)
    for i in range(-1,2):
        if 0<y+i<6 and i!=0:
            change_status(y+i,x)
    for i in range(-1,2):
        if 0<x+i<6 and i!=0:
            change_status(y,x+i)
    
    set_field()

    if check_field():
        break

print("ゲームクリア")
