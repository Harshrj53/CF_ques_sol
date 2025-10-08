def func(n,arr):
    minn=min(arr)
    ans=0
    for i in range(n):
        ans+=(arr[i]-minn)
    return ans 
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(func(n,arr))
