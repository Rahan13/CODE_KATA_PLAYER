vals=input().split()
ar1=input().split()
ar1=list(map(int,ar1))
ar2=input().split()
ar2=list(map(int,ar2))
for i in range(len(ar2)):
    ar1.append(ar2[i])
    print(max(ar1),end=" ")
