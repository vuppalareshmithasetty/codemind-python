n=input()
d={}
z=0
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]>1:
        z=10
    else:
        pass
if(z==10):
    print("Not Unique Number")
else:
    print("Unique Number")
    