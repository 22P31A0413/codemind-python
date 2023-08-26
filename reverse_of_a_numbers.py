n=int(input())
s=0
while True:
    r=n%10
    n=n//10
    s=s*10+r
    if(n==0):
        break
print(s)