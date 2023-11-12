n=int(input())
l=list(map(int,input().split()))
z=set(l)
y=z.intersection(z)
x=list(y)
s=0
for i in range(len(x)):
    s=s+x[i]
print(s)