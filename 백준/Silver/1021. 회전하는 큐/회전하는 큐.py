# https://www.acmicpc.net/problem/1021
from collections import deque

def left_move(q):
    q.append(q.popleft())
    return q

def right_move(q):
    q.appendleft(q.pop())
    return q

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = deque(list(range(1, n + 1)))
t = 0
for num in nums:
    idx = q.index(num)
    k = len(q)
    # 1 2(1 - 9) 3 4 5 6 7 8 9 10 
    # 2을 뽑기 위해서는 왼쪽으로 1번을 돌리거나 오른쪽으로 9번을 돌려야함.
    # 1번은 2의 인덱스를 의미함.
    # 9번은 총 길이에서 왼쪽으로 돌리는 횟수를 뺀 것을 의미함.
    if idx < k - idx:
        for _ in range(idx):
            q = left_move(q)
            t += 1
    else:
        for _ in range(k - idx):
            q = right_move(q)
            t += 1
    q.popleft()
    
print(t)