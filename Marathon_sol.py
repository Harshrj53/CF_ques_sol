t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    a=arr[0]
    count=0
    for i in range(len(arr)):
        if arr[i]>a:
            count+=1
    print(count)        
        
