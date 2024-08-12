a, b, c = sorted(list(map(int, input().split())))

if a == b and b == c and a == c:
    print(2)
elif c ** 2 == a ** 2 + b ** 2:
    print(1)
else:
    print(0)