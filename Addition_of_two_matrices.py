n=int(input())
mat1=[]
mat2=[]
for i in range(n):
    i=list(map(int,input().split()))
    mat1.append(i)
for j in range(n):
    j=list(map(int,input().split()))
    mat2.append(j)
for a in range(n):
    for b in range(n):
        print(mat1[a][b]+mat2[a][b],end=' ')
    print()