num=int(input())
count=0
i=0
while(i<n):
    val=input().split()
    if val[0]<val[1]:
        count+=1
    i+=1
print(count)
