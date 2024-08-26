n = int(input())
menus = [int(input()) for _ in range(n)]
m = int(input())
wants = [int(input()) for _ in range(m)]

sum_val = 0
for want in wants:
    sum_val += menus[want - 1]
    
print(sum_val)