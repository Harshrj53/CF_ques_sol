t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    total=a+b+c
    if total%3!=0:
        print("NO")
        continue
    x=total//3
    if (a<=x<=c) and (b<=x<=c) :
        print("YES")
    else:
        print("NO")
