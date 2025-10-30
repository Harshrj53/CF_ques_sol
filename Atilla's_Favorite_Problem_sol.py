def func(n,arr):
    maxx=max(arr)
    return ord(maxx)-ord('a')+1
    
t=int(input())
for _ in range(t):
    n=int(input())
    arr=input()
    print(func(n,arr))
