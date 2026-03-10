n = int(input())

std = 'WOW'

for _ in range(n):
    s = input()
    l = len(s)
    cnt = 0
    for idx in range(l):
        if s[idx: idx + 3] == std:
            cnt += 1
    print(cnt)