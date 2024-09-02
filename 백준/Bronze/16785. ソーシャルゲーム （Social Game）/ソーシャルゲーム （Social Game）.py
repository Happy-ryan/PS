A, B, C = map(int, input().split())

sum_val = 0
total = 0

while total < C:
    total += A
    sum_val += 1
    if sum_val % 7 == 0:
        total += B
        
print(sum_val)