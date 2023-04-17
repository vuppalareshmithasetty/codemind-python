r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        s=s+mat[i][j]
print(s)
    