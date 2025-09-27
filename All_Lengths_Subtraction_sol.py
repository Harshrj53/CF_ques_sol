t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().split()))
    l, r, need = 0, n - 1, 1
    possible = True
    while need <= n:
        if p[l] == need:
            l += 1
        elif p[r] == need:
            r -= 1
        else:
            possible = False
            break
        need += 1
    print("YES" if possible else "NO")
