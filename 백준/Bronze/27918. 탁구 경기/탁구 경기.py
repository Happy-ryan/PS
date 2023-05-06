sum_d = 0
sum_p = 0
round = int(input())
flag = False
for _ in range(round):
    x = input()
    if x == "D":
        sum_d += 1
    else:
        sum_p += 1
    
    if abs(sum_d - sum_p) >= 2:
        break
    
print(f"{sum_d}:{sum_p}")