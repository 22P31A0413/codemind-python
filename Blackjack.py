x,y=map(int,input().split())
z=21-(x+y)
if(x>=1 and x<=10 and y>=1 and y<=10 and z>=1 and z<=10):
    print(z)
else:
    print("-1")