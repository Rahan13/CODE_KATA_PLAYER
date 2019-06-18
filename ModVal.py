s=input().split()
if int(s[0])%int(s[1])==0:
    print(s[0])
elif int(s[1])%int(s[0])==0:
    print(s[1])
else:
    print(int(s[0])*int(s[1]))
