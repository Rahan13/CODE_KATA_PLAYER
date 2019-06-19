n=int(input())
stgs=input().split()
out=dict()
for i in range(len(stgs)):
    a=list()
    if len(stgs[i]) not in out:
        a.append(stgs[i])
        out.update({len(stgs[i]):a})
    else:
        a=out[len(stgs[i])]
        a.append(stgs[i])
        out.update({len(stgs[i]):a})
[[print(i,end=" ") for i in sorted(out[l])] for l in out]
