n=int(input())
hrs=n//3600
rem=n%3600
minn=rem//60
rem1=rem%60
print("H:M:S-%d:%d:%d"%(hrs,minn,rem1))