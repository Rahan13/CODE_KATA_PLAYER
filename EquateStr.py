inp=input().split()
leng=int(inp[2])
inp.remove(str(leng))
if len(inp[0])!=len(inp[1]):
    print("no")
elif inp[0]==inp[1]:
    print("yes")
else:
    a=True
    i=0
    l=len(inp[0])
    while(i<=l):
        ch=inp[0][i]
        if inp[0].count(ch) != inp[1].count(ch):
            l-=inp[0].count(ch)
            leng -= abs(inp[0].count(ch)-inp[1].count(ch))
            inp[0].replace("",ch)
            inp[1].replace("",ch)
        if leng<0:
            a=False
            print("no")
        i+=1
    if a:
        print("yes")
