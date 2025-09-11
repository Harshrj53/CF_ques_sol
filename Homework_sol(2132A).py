t=int(input())
for i in range(t):
    n=int(input())
    a=input().strip()
    m=int(input())
    b=input().strip()
    c=input().strip()
    ans=a
    for i in range(m):
        if c[i]=='V':
            ans=b[i]+ans
        else:
            ans=ans+b[i]
    print(ans)    
