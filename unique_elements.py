n=int(input())
l=list(map(int,input().split()))
ans=[]
for i in range(n):
    if l[i]  not in ans:
        ans.append(l[i])
for i in range(len(ans)):
    print(ans[i],end=" ")