inp = input()
val = input().split("0")
st = ""
for i in range(0,len(val)):
    if i%2==0:
        st = st+val[i]
st = st + val[len(val)-1]
st = list(st)
print(" ".join(st))
