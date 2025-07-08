year = input("生まれた年を入力してください")
month = input("生まれた月を入力してください")
day = input("生まれた日を入力してください")
s = year + month + day
n = 0

for i in s:
    n += int(i)

if n >= 10:
    n = n//10 + n%10 

print(f"あなたの運命数は{n}です")
