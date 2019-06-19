p1=input().split()
p2=input().split()
p3=input().split()
if int(p1[0])==int(p2[0]) and int(p2[0])==int(p3[0]):
    print("yes")
elif int(p1[1])==int(p2[1]) and int(p2[1])==int(p3[1]):
    print("yes")
else:
    print("no")
