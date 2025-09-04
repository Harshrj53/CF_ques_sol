t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n==1 or n==2:
        print(1)
    else:    
        count=2
        start=3
        end=start+x-1
        while True:
            if start <= n<=end:
                print(count)
                break
            else:
                start+=x
                end+=x
                count+=1
