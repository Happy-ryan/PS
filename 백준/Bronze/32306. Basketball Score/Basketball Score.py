a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

def getScore(a, b, c):
    return a * 1 + b * 2 + c * 3

val1 = getScore(a1, b1, c1)
val2 = getScore(a2, b2, c2)

if val1 > val2:
    print(1)
elif val1 < val2:
    print(2)
else:
    print(0)