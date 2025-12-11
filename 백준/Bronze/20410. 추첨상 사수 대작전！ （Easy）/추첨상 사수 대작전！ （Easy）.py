m, seed, x1, x2 = map(int, input().split())

def solution(m, seed, x1, x2):
    for a in range(m):
        for c in range(m):
            if (a*seed + c) % m == x1 and (a*x1 + c) % m == x2:
                return (a, c)


print(*solution(m, seed, x1, x2))
