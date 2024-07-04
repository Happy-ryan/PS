s = input()

def digit_sum(x: int):
    sum_val = 0
    while x > 0:
        sum_val += x % 10
        x //= 10
        
    return sum_val

for x in s:
    cnt = digit_sum(ord(x))
    for _ in range(cnt):
        print(x, end='')
    print()