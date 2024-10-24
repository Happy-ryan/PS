n = int(input())
# n = 3 * 2**(62)
k = 64
for _ in range(1, 65):
    if n % 2 != 0:
        print(k)
        break
    else:
        n //= 2
        k -= 1