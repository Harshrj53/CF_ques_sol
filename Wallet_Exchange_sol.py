t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if (a%2)!=(b%2):
        print("Alice")
    else:
        print("Bob")
