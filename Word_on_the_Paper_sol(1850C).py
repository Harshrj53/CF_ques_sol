t=int(input())
for i in range(t):
    ch=[input().strip() for _ in range(8)]
    l=[]
    for j in range(len(ch)):
        for k in range(len(ch[j])):
            if ch[j][k]!='.':
                l.append(ch[j][k])
            
    print(*l,sep="") 
