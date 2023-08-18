a=int(input())
if(a<=10000):
    d=(0.8*a)+(0.2*a)+a
elif(a<=20000):
    d=(0.9*a)+(0.25*a)+a
elif(a>20000):
    d=(0.95*a)+(0.3*a)+a
print(f"{d:.2f}")