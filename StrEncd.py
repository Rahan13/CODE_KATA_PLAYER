s1=input().lower()
n=3
s="abcdefghijklmnopqrstuvwxyz"
alpha=dict()
for i in range(len(s)):
    pos=(i+n)%len(s)
    alpha.update({s[i]:s[pos]})
for i in range(len(s1)):
    print(alpha[s1[i]].upper(),end="")

