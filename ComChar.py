inp = input().split()
a = True
for i in range(0,len(inp[0])):
    if inp[0][i] in inp[1]:
        a = False
        print("yes")
        break
if a:
    print("no")
