n=int(input())
a=input().split()
b=input().split()
c=list()
for i in range(n):
    if a[i] in b and c.count(a[i])==0:
       c.append(a[i])
{print(x,end=" ") for x in c}
