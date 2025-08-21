t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    num=list(map(int,input().split()))
    l=[]
    maxx=float("-inf")
    l.append(0)
    l.extend(num)
    l.append(x)
    l.sort()
    for i in range(len(l)-1):
        if l[i+1]-l[i]>maxx:
            maxx=l[i+1]-l[i]
    maxx=max(maxx,2*(x-l[-2]))        
    print(maxx) 
