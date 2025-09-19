t = int(input().strip())
for _ in range(t):
    l, r = map(int, input().split())
    ans = 1 if l <= 1 <= r else 0
    if r >= 2:
        ans += max(0, r - max(l, 2))
    print(ans)
