def solution(n, m, b):
    year = 0
    while True:
        if n > m:
            return year
        year += 1
        n *= (1 + b / 100)

try:
    while True:
        n, b, m= map(float, input().split())
        print(solution(n, m, b))
except:
    exit