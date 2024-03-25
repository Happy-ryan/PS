N, M = map(int,input().split())
data = list(map(int,input().split()))

cnt = 0
sum = 0
e = 0

for s in range(N):
  while sum < M and e < N:
    sum += data[e]
    e += 1
  if sum == M:
    cnt += 1
  sum -= data[s]

print(cnt)