p,c,b,m,cs=map(int,input().split())
g=(p+c+b+m+cs)//5
if(g>=90):
    print("Grade A")
elif(g>=80):
    print("Grade B")
elif(g>=70):
    print("Grade C")
elif(g>=60):
    print("Grade D")
elif(g>=40):
    print("Grade E")
elif(g<40):
    print("Grade F")