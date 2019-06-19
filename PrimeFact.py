s=int(input())
fact=list()
for i in range(2,s+1):
    if s%i==0:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            fact.append(i)
sorted(fact)
[print(f,end=" ") for f in fact]

