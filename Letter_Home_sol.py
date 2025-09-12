t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    xs = list(map(int, input().split()))
    L, R = xs[0], xs[-1]   
    ans = min(abs(s - L), abs(s - R)) + (R - L)
    print(ans)
