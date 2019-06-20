s=input().split()
nums=input().split()
nums=list(map(int,nums))
if int(s[1]) in nums:
    print("Yes")
else:
    print("No")
