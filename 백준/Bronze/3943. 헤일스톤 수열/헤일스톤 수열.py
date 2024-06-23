import sys

input = sys.stdin.readline

t = int(input())

def solution(x):
    ans = x
    while True:
        if x == 1:
            ans = max(ans, x)
            break
        else:
            if x % 2 == 0:
                x //= 2
            else:
                x *= 3
                x += 1
            ans = max(ans, x)
    return ans


for _ in range(t):
    x = int(input())
    print(solution(x))