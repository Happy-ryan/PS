n = int(input())

p = 0
temp = n
while temp % 2 == 0:
    temp //= 2
    p += 1

if temp * (2 ** p) == n:
    print(temp, p)