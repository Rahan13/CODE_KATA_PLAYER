def checckIso(s1,s2):
    if len(s1) != len(s2):
        print("no")
        return
    for i in range(0,len(s1)):
        if s1.count(s1[i]) == s2.count(s2[i]):
            continue
        else:
            print("no")
            return
    print("yes")
    
strs=input().split()
checckIso(strs[0],strs[1])
