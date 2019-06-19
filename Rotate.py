s=input().split()
nums=input().split()
d=dict()
for i in range(0,len(nums)):
    pos=0
    if (i+int(s[1]))<len(nums):
        pos=i+int(s[1])
    else:
        pos=i%int(s[1])
    d.update({pos:nums[i]})
[print(d[i],end=" ") for i in d]
