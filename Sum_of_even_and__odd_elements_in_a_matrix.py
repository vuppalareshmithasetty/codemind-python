r,c=map(int,input().split())
mat=[]
s=0
q=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            s=s+mat[i][j]
        else:
            q=q+mat[i][j]
print(s,q)