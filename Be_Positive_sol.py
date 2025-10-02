t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    neg=arr.count(-1)
    zeroes=arr.count(0)
    
    ans=zeroes
    
    if neg%2==1:
        ans+=2
    print(ans)    
