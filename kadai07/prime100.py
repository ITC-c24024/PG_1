r=0
prime=True

for i in range(2,100):
    prime=True
    for n in range(2,i+1):
        if i!=n:
            if i%n==0:
                prime=False
                break
    if prime:
        print(i,end=" ")
        r+=1
    if r==10:
        print("")
        r=0
print("")
