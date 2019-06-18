s=int(input())
val=0
while(s>0):
    val=val+((s%10)**2)
    s=int(s/10)
print(val)
