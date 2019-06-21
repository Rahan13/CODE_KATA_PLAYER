strgs=input().split()
s1=list(strgs[0])
d=dict()
for i in range(0,len(s1)):
    pos=(i+int(strgs[1]))%len(s1)
    d.update({pos:s1[i]})
[print(d[i],end=" ") for i in d]
