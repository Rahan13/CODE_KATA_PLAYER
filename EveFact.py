numb=int(input())
for i in range(1,numb+1):
    if numb%i==0 and i%2==0:
        print(i,end=" ")
