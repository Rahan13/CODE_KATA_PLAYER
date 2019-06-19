s=input().split()
nums=input().split()
d=dict()
for i in range(0,len(nums)):
    pos=(i+int(s[1]))%int(s[0])
    d.update({pos:nums[i]})
[print(d[i],end=" ") for i in d]
