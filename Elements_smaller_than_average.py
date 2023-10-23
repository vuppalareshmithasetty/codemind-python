n=int(input())
l=list(map(int,input().split()))
s=0;ans=0
for i in range(n):
    s=s+l[i]
avg=s//n
for i in range(n):
    if l[i]<=avg:
        ans=ans+1
print(ans)