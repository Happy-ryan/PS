# https://www.acmicpc.net/problem/1806
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
sum = 0
e = 0
ans = int(1e9)

for s in range(N):
    while e < N and sum < M:
        sum += data[e]
        e += 1
    if sum >= M:
        ans = min(ans, e - s)
    sum -= data[s]
if ans == int(1e9): print(0)
else: print(ans)