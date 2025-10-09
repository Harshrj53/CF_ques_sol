def func(n,arr):
    unique_count=len(set(arr))
    if (n-unique_count)%2==0:
        return unique_count
    else:
        return unique_count-1
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(func(n,arr))
