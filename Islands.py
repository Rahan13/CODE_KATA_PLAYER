n=int(input())
mat=list(list())
i=0
while(i<n):
    row=input().split()
    mat.append(row)
    i+=1
island=0
for j in range(n):
    for k in range(n):
        a=False
        if mat[j][k]==str(1):
            a=True
            if k+1<n and mat[j][k+1]!=str(0):
                a=False
            if k-1>=0 and mat[j][k-1]!=str(0):
                a=False
            if j+1<n and mat[j+1][k]!=str(0):
                a=False
            if j-1>=0 and mat[j-1][k]!=str(0):
                a=False
        if a:
            island+=1
print(island)
