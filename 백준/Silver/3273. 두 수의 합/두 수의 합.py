import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int,input().split())))
# 주어진 입력을 정렬해도 문제가 없을지 확인하기
x = int(input())

cnt = 0
sum = 0
r = n-1

for l in range(n):
  while r >0  and a[l]+a[r] > x: # 정렬한 상태/ r-끝점 /r -= 1 : 두 쌍의 합이 작아진다. 즉 두 쌍의 합이 x보다 크다를 의미함. 따라서 부등호 방향 a[l]+a[r]>x가 되는 것
    sum += a[r] # a[l] + a[r] < x x보다 작다는 거니까  r+=1이되어야하는데 r은 n-1끝점이다. 그러므로 불가능
    r -= 1
  if l < r and a[l] + a[r] == x:
    cnt += 1

print(cnt)