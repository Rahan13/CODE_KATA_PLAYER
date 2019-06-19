nums=input().split()
nums=list(map(int,nums))
mac=0
for i in range(1,min(nums)+1):
    if nums[0]%i ==0 and nums[1]%i==0 and i>mac:
        mac=i
print(mac)
