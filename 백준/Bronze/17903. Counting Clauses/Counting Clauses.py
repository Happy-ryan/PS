def f(m):
    if m >= 8:
        return "satisfactory"
    return "unsatisfactory"

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
print(f(m))