import sys
input = sys.stdin.readline

N,M = map(int,input().split()) 
ans = []
visited = [False]*(N+1)

def back(n):
  if n == M: # M : 깊이를 나타냄
    print(' '.join(map(str,ans)))
    return
  
  for i in range(1,N+1):
    if not visited[i]:
      visited[i] = True
      ans.append(i)
      back(n+1)
      visited[i] = False
      ans.pop()

back(0)
  