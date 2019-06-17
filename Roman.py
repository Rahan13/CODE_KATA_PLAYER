dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
inp=input()
val=0
val_list=list()
for i in range(0,len(inp)):
    val_list.append(inp[i])
    if inp[i]=="V":
        val=val-(2*val_list.count("I"))
        if val_list.count("I")>0:
            val_list.remove("I")
    if inp[i]=="X":
        val=val-2*(val_list.count("V")+val_list.count("I"))
        if val_list.count("I")>0:
            val_list.remove("I")
        if val_list.count("V")>0:
            val_list.remove("V")
    val=val+dic[inp[i]] 
print(val)
