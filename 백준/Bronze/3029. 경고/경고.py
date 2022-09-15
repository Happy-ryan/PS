
import sys

input = sys.stdin.readline

def second_change(arr):
  second = arr[0]*3600 + arr[1]*60 + arr[2]
  return second

def rechange(n):
  A = n // 3600
  n -= A*3600
  B = n//60
  n -= B*60
  C = n
  if A < 10:
    h = '0'+str(A)
  else:
    h = A
  if B < 10:
    m = '0'+str(B)
  else:
    m = B
  if C < 10:
    s = '0'+str(C)
  else:
    s = C 
  return h,m,s


cur = list(map(int,input().split(':')))
bomb = list(map(int,input().split(':')))
# 시간 문제 기준 : 0시 0분 0초 
sub = second_change(bomb) - second_change(cur)

if sub <= 0:
  a = second_change(bomb) + 24*3600
  b = second_change(cur)
  print(f'{rechange(a-b)[0]}:{rechange(a-b)[1]}:{rechange(a-b)[2]}')
else:
  print(f'{rechange(sub)[0]}:{rechange(sub)[1]}:{rechange(sub)[2]}')