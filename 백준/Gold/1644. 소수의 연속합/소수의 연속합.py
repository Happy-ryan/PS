
import sys

input = sys.stdin.readline

# 에라토스테네스 체 - 함수
def f(n):
  a = [False,False]+[True]*(n-1) # [숫자0,1-소수아님]+[인덱스2~n-소수라고 가정]
  primes = []

  for i in range(2,n+1):
    if a[i]:
      primes.append(i)
      for j in range(2*i,n+1,i):
        a[j] = False

  return primes

N = int(input())
data = f(N)

cnt = 0
sum = 0
e = 0

for s in range(len(data)):
  while sum < N and e < len(data):
    sum += data[e]
    e += 1

  if sum == N:
    cnt += 1
  sum -= data[s]

print(cnt)