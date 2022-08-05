n = int(input())
arr = [input().split() for _ in range(n)]
def f(row):
    result = []
    for s in reversed(row):
        result.append(s)
    return result

i = 1
for row in arr:
    print("Case #{0}:".format(i),*f(row))
    i+=1