t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    if a==n and b==n:
        print("Yes")
    elif a==n or b==n:
        print("No")
    elif a+b <=n-2:
        print("Yes")
    else:
        print("No")
