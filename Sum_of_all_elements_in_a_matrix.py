r,c=map(int,input().split())
mat=[]
for i in range(r):
    x=list(map(int,input().split()))
    mat.append(x)
s=0
for x in mat:
    for j in x:
        s=s+j
print(s)