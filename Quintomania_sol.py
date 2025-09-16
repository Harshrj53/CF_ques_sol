t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    perfect = True
    for i in range(1, n):
        if abs(arr[i] - arr[i-1]) not in (5, 7):
            perfect = False
            break
    
    if perfect:
        print("YES")
    else:
        print("NO")
