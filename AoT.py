angles = input().split()
angles = list(map(int,angles))
if 0 in angles:
    print("no")
else:
    val = sum(angles)
    if val == 180:
        print("yes")
    else:
        print("no")
