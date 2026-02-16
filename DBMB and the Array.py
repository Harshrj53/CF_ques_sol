t = int(input())
for _ in range(t):
    n, s, x = map(int, input().split())
    arr = list(map(int, input().split()))
    
    current_sum = sum(arr)
    
    if s >= current_sum and (s - current_sum) % x == 0:
        print("YES")
    else:
        print("NO")
