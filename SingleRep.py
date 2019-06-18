s=input()
m=0
for i in range(0,len(s)):
    if s.count(s[i])==1:
        print(s[i])
        break
