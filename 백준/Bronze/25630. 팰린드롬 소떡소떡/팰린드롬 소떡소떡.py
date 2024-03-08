n = int(input())
s = input()


def solution(n, s):
    cnt = 0
    for idx in range(n // 2):
        if s[idx] != s[n - idx - 1]:
            cnt += 1
    return cnt


print(solution(n, s))