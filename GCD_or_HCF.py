x,y=map(int,input().split())
for i in range(1,x+1 and y+1):
    if(x%i==0 and y%i==0):
        q=[i]
print(max(q))