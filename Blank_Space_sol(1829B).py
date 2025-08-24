t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    count = 0
    
    longest=0
    current=0
    
    for val in num:
        if val==0:
            current+=1
            longest=max(current,longest)
        else:
            current=0
    print(longest)
