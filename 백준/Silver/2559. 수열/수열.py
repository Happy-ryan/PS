
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
a = list(map(int,input().split()))

window = sum(a[0:K])# 누적합을 받아줄 변수가 window이다.

res = window
for x in range(K,N):
  window -= a[x-K] 
  window += a[x]
  res = max(res,window) # window의 누적합을 갱신

print(res)