t=int(input())
for i in range(t):
    strr=list(input())
    count_a=0
    count_b=0
    for j in range(len(strr)):
        if strr[j]=="A":
            count_a+=1
        else:
            count_b+=1
    if count_a>count_b:
        print("A")
    else:
        print("B")
