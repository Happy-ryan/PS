n = int(input())

sum_val = 0
sum_val2 = 0

for num in range(1, n + 1):
    sum_val += num
    sum_val2 += num ** 3

print(sum_val)
print(sum_val * sum_val)
print(sum_val2)