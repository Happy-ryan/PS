t = int(input())

def solution(r, c, k):
    for _ in range(k):
        if r >= c:
            r //= 2
        else:
            c //= 2
    return max(r, c), min(r, c)

for _ in range(t):
    r, c, k = map(int, input().split())
    print(f'Data set: {r} {c} {k}')
    print(solution(r, c, k)[0], solution(r, c, k)[1])
    print()