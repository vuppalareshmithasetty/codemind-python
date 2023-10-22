n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if l[i]%2==0:
        ff=i
        break
for i in range(n-1,0,-1):
    if l[i]%2==0:
        ll=i
        break
for i in range(n):
    if i>ff and i<ll:
        if l[i]%2!=0:
            c=c+1
print(c)