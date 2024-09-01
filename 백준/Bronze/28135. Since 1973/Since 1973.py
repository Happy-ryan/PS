n = int(input())

sum_val = 0
for i in range(n):
    sum_val += 1
    if '50' in str(i):
        sum_val += 1

print(sum_val)