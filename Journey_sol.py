t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    cycle = a + b + c
 
    
    full_cycles = (n - 1) // cycle      
    ans = full_cycles * cycle           
    days = full_cycles * 3              
 
    
    remaining = n - ans
    if remaining <= a:
        days += 1
    elif remaining <= a + b:
        days += 2
    else:
        days += 3
 
    print(days)
