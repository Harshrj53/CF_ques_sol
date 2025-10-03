import math
 
t=int(input())
for _ in range(t):
    s=input().strip()
    n=int(s)
    
    k=int(math.isqrt(n))
    
    if k*k!=n:
        print(-1)
    else:
        if len(s)==4:
            a=int(s[:2])
            b=int(s[2:])
            if a+b==k:
                print(a,b)
                continue
        print(0,k)
