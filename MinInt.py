n=int(input())
if n%2!=0:
    print("1")
else:
    for i in range(2,n):
        if n%i==0 and int(n/i)%2!=0:
            print(i)
            break
