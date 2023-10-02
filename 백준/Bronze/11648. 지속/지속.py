n = int(input())

def f(level, n):
    if n < 10:
        return level
    num = 1
    for x in str(n):
        num *= int(x) 

    return f(level + 1, num)

print(f(0, n))