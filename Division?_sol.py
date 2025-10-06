def rating(n):
    if n<=1399:
        return "Division 4"
    elif n>=1400 and n<=1599:
        return "Division 3"
    elif n>=1600 and n<=1899:
        return "Division 2"
    else:
        return "Division 1"
 
 
 
t=int(input())
for i in range(t):
    n=int(input())
    print(rating(n))
