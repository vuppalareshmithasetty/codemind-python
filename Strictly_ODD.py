n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2!=0:
        if i%2==0:
            c=c+1
if c>0:
    print("False")
else:
    print("True")