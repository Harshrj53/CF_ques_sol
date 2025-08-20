t=int(input())
for i in range(t):
    a,b=list(input().split())
    first_ch_a=a[0]
    remaining_ch_a=a[1:]
    first_ch_b=b[0]
    remaining_ch_b=b[1:]   
    new_a=first_ch_b+remaining_ch_a
    new_b=first_ch_a+remaining_ch_b
    print(new_a,new_b) 
