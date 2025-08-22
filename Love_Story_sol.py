t=int(input())
a=["c","o","d","e","f","o","r","c","e","s"]
for i in range(t):
    s=list(input())
    count=0
    for j in range(len(s)):
        if s[j]==a[j]:
            j+=1
        else:
            count+=1
    print(count) 
