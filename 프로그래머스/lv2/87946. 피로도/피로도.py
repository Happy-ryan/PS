from itertools import permutations
# 순열 > 백트래킹으로 가능
answer = 0

def f(k, tup):
    cnt = 0
    for row in tup:
        if k >= row[0]:
            k -= row[1]
            cnt += 1
        else:
            break
    return cnt

def dfs(lev, d, dungeons, used, visited, k):
    global answer
    if lev == d:
        a = visited.copy()
        answer = max(answer, f(k, a))
    for i,row in enumerate(dungeons):
        if used[i] == 0:
            used[i] = 1
            visited.append(row)
            dfs(lev + 1, d, dungeons, used, visited, k)
            used[i] = 0
            visited.pop()
            
def solution(k, dungeons):
    visited = []
    used = [0] * len(dungeons)
    dfs(0, len(dungeons), dungeons, used, visited, k)
    return answer