t=int(input())
for i in range(t):
    n=int(input())
    name=input().strip()
    if sorted(name) == sorted("Timur"):
        print("Yes")
    else:
        print("No")
