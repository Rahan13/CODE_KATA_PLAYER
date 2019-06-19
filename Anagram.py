stg={"k":1,"a":2,"b":1,"l":1,"i":1}
s=int(input())
strgs=list()
for i in range(s):
    strgs.append(input())
count=0
for i in range(s):
    a=True
    if len(strgs[i]) != 6:
        continue
    for c in range(0,len(strgs[i])):
        if strgs[i].count(strgs[i][c])!=stg[strgs[i][c]]:
            a=False
            break
    if a:
        count+=1
print(count)
