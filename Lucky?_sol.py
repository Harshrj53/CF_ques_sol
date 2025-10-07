def lucky_ticket(n):
    first_half=0
    last_half=0
    for i in range(0,3):
        first_half+=int(n[i])
    for j in range(3,6):
        last_half+=int(n[j])
    if first_half==last_half:
        return "YES"
    else:
        return "NO"
t=int(input())
for i in range(t):
    n=str(input())
    print(lucky_ticket(n))
