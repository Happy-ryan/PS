g, p, t = map(int, input().split())

one, group = g * p, g + p * t

if one < group:
    print(1)
elif one > group:
    print(2)
else:
    print(0)