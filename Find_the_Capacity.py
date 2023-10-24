s,t,b=map(int,input().split())
c=2*s*t*b*512
ans=c//1024
print("%dKB"%(ans))