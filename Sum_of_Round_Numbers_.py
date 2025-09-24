t = int(input())
for _ in range(t):
    n = input().strip()
    ans = []
    p = 1
    for d in n[::-1]:         
        if d != '0':
            ans.append(int(d)*p)
        p *= 10
    print(len(ans))
    print(*ans[::-1]) 
