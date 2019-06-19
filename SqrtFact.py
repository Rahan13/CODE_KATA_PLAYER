nums=input().split()
num1=list(range(1,int(nums[1])+1))
num1=list(map(float,num1))
count=0
for i in range(int(nums[0]),int(nums[1])+1):
    val=i**0.5
    if val in num1:
        count+=1
print(count)
