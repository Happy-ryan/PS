n = int(input())
c = int(input())
sum_val = n * 50 - c * 10
sum_val += 500 if n > c else 0
print(sum_val)