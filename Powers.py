num=input().split()
num=list(map(int,num))
if num[0]%num[1] !=0:
    print("no")
else:
    while(True):
        num[0]=int(num[0]/num[1])
        if num[0]==num[1] or num[0]==1:
            print("yes")
            break
        if num[0]==0 or num[0]%num[1]!=0:
            print("no")
            break
