P, Q = map(int, input().split())

def get_divisor(num):
    nums = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            nums.append(i)
            if i ** 2 != num:
                nums.append(num // i)
    
    nums.sort()
    return nums

Ps = get_divisor(P)
Qs = get_divisor(Q)

for p in Ps:
    for q in Qs:
        print(f"{p} {q}")