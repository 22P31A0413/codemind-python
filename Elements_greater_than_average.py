n=int(input())
x=list(map(int,input().split()))
a=sum(x)//n
c=0
for i in x:
    if i>=a:
        c=c+1
print(c)