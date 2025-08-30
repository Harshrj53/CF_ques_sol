n=int(input())
num=list(map(int,input().split()))
ans="Easy"
for i in range(n):
    if num[i]==1:
        ans="Hard"
        break
    else:
        ans = "Easy"
print(ans)  
