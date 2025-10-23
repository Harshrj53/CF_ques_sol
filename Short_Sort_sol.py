def can_abc(s):
    if s[0]=="a" and s[1]=="b" and s[2]=="c":
        return "YES"
    s=list(s)
    for i in range(3):
        for j in range(i+1,3):
            s[i],s[j]=s[j],s[i]
            if s[0]=="a" and s[1]=="b" and s[2]=="c":
                return "YES"
            s[i],s[j]=s[j],s[i]
    return "NO"
t=int(input())
for i in range(t):
    s=input().strip()
    print(can_abc(s))
            
