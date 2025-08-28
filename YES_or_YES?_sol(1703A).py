t = int(input())
for _ in range(t):
    arr = input().strip()
    if len(arr) >= 3 and arr[0].lower() == "y" and arr[1].lower() == "e" and arr[2].lower() == "s":
        print("Yes")
    else:
        print("No")
