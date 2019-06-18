s=input()
mac=""
m=0
for i in range(0,len(s)):
    if s.count(s[i])>m:
        mac=s[i]
        m=s.count(s[i])
print(mac)
