n=int(input())
m=int(input())
for i in range(n,m+1):
    j=i
    d=0
    c=0
    while(j!=0):
        r=j%10
        if(r!=0 and i%r==0):
            d=d+1
        j=j//10
        c=c+1
    if(c==d):
        print(i,end=" ")