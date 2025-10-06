def candies(n):
    return (3-(n%3))%3
    
t=int(input())
for i in range(t):
    n=int(input())
    print(candies(n))
