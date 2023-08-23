n=int(input())
m=n*n
z=0
while(m):
    s=m%10;
    z=s+z
    m=m//10
if(n==z):
    print("Neon Number")
else:
    print("Not Neon Number")