n=int(input())
a=0
b=1
yes=0
while(b):
    c=a+b
    if c==n:
        yes=yes+1
        break
    elif c>n:
        break
    else:
        pass
    a=b
    b=c
if(yes==1):
    print("True")
else:
    print("False")