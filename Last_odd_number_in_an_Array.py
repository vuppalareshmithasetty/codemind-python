n=int(input())
l=list(map(int,input().split()))
for i in range((n-1),0,-1):
    if l[i]%2!=0:
        print(l[i])
        break