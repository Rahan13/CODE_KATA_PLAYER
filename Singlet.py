s=list(str(input()).split())
s="".join(s)
l=len(s)
i=0
while(i<l):
    if s.lower().count(s[i].lower())==1:
        print(s[i],end=" ")
        s.replace(s[i],"")
        l=len(s)
    i+=1
