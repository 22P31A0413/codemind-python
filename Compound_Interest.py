p=float(input())
r=float(input())
t=float(input())
ci=p*pow((1+r/100),t)
a=ci-p
print(f"{a:.2f}")