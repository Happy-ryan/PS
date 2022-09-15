
import sys

input = sys.stdin.readline

N, M = map(int,input().split())
data = list(map(int,input().split()))

cnt = 0
sum = 0
e = 0
ans = []

for s in range(N):
  while sum < M and e < N:
    sum += data[e]
    e += 1
  if sum >= M:
    cnt += 1
    sub = e - s
    ans.append(sub)
  sum -= data[s]

if cnt == 0:
  print(0)
else:
  print(min(ans))