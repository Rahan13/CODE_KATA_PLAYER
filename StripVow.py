s=str(input())
vowels="aeiou"
i=len(s)-1
while(i>=0):
    if s[i] in vowels:
        i-=1
        continue
    print(s[i],end="")
    i-=1
