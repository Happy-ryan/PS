n = int(input())
arr = [input().split() for _ in range(n)]
def f(row):
    if sorted(row[0]) == sorted(row[1]):
        return "Possible"
    else:
        return "Impossible"

for row in arr:
    print(f(row))
