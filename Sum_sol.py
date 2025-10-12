def func(a,b,c):
    if a+b==c or b+c==a or c+a==b:
        return "YES"
    else:
        return "NO"
    
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    print(func(a,b,c))
