import sys
input = sys.stdin.readline
heights = sorted([int(input()) for row in range(9)])
res = []
# 9개의 키 중 7개의 키의 합이 반드시 100인 것이 존재
# 7개의 합을 찾지 말고 9개 전체 키의 합에서 2개를 빼서 100이 되는 것을 찾자.
for x in range(9):
  for y in range(9):
    if x != y:
      sub = heights[x] + heights[y]
      if sum(heights) - sub == 100:
        res.append((x,y))

for k in range(9):
  if k in res[-1]:
    continue
  print(heights[k])