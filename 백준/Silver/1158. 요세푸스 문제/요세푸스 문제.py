# https://www.acmicpc.net/problem/1158
from collections import deque

def rotate():
    for _ in range(k - 1):
        e = dq.popleft()
        dq.append(e)
    return dq.popleft()

n, k = map(int, input().split())
dq = deque(range(1, n + 1))

res = '<'
for i in range(n):
    e = rotate()
    if i == n - 1:
        res += f"{e}>"
    else:
        res += f"{e}, "
        
print(res)
# 1 2 3 4 5 6 7
# (3) 4 5 6 7 1 2 : k가 3일 때 회전은 2번 발생..
# (6) 7 1 2 4 5
# (2) 4 5 7 1
# (7) 1 4 5
# (5) 1 4
# (1) 4
# (4)