# https://www.acmicpc.net/problem/4084

def solution(a, b, c, d):
    cnt = 0
    while True:
        if (a == b) and (a == c) and (a == d) and (b == c) and (b == d) and (c == d):
            break
        x = abs(a - b)
        y = abs(b - c)
        w = abs(c - d)
        z = abs(d - a)
        a, b, c, d = x, y, w, z
        cnt += 1
    return cnt

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    print(solution(a, b, c, d))