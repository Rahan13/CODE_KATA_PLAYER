num = int(input())
a = True
for i in range(2,num):
    if num%i ==0:
        a = False
        print("yes")
        break
if a:
    print("no")
