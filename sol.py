t=int(input())
for i in range(t):
    x1,x2,x3=map(int,input().split())
    sn1=abs(x1-x2) + abs(x1-x3)
    sn2=abs(x2-x1) + abs(x2-x3)
    sn3=abs(x3-x1) + abs(x3-x2)
    if sn1 <= sn2 and sn1 <= sn3:
        print(sn1)
    elif sn2 <= sn1 and sn2 <= sn3:
        print(sn2)
    elif sn3 <=sn1 and sn3 <= sn2:
        print(sn3)
