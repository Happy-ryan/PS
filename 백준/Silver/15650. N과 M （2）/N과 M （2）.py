import sys
input = sys.stdin.readline

N,M = map(int,input().split()) 
ans = []
visited = [False]*(N+1)
ans_list = []

def back(n):
  if n == M: # M : 깊이를 나타냄
    # res = ' '.join(map(str,ans))
    res = ans.copy() # 왜 카피 할 때와 안 할 때 차이가 있는 것일까
    ans_list.append(res)
    return
  
  for i in range(1,N+1):
    if not visited[i]:
      visited[i] = True
      ans.append(i)
      back(n+1)
      visited[i] = False
      ans.pop()

  return ans_list

check = []
for li in back(0):
  if sorted(li) not in check:
    check.append(li)

for k in check:
  print(' '.join(map(str,k)))