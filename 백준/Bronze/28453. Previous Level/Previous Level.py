def check(level):
    if level >= 300:
        return 1
    if level >= 275:
        return 2
    if level >= 250:
        return 3
    return 4


n = int(input())
levels = list(map(int, input().split()))
for level in levels:
    print(check(level), end = ' ')