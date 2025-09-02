t=int(input())
for i in range(t):
    arr=input().strip()
    n=len(arr)
    if n%2!=0:
        print("No")
    else:
        half=n//2
        if arr[:half]==arr[half:]:
            print("Yes")
        else:
            print("No")
