r,c=map(int,input().split())
mat=[]
s=0
a=0
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
for j in range(r):
    for k in range(c):
        if(j%2==0):
            s=s+mat[j][k]
        else:
            a=a+mat[j][k]
print(s,a)