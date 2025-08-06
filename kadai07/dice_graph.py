import random

result=[0]*6

for _ in range(0,100):
    n=random.randint(0,len(result))
    result[n-1]+=1

for i in range(len(result)):
    print(f"{i+1}：{"*"*result[i]}")
