t=int(input())
for i in range(t):
    a,b,c,x,y=map(int,input().split())
    
    dog_need=max(0,x-a)
    cat_need=max(0,y-b)
    
    if dog_need+cat_need<=c:
        print("Yes")
    else:
        print("No")
    
