N, S = map(int, input().split())
num = list(map(int, input().split()))
used = [0] * N
visited = []
idx = [0]
cnt = 0

# d 부분집합의 원소의 개수 1 <= d <= N
def dfs(lev, S, d):
    global cnt
    if lev == d:
        if sum(visited) == S:
            # print(visited)
            cnt += 1
            return
        else:
            return
    for i in range(idx[-1], N):
        if used[i] == 0:
            used[i] = 1
            visited.append(num[i])
            idx.append(i)
            dfs(lev + 1, S, d)
            used[i] = 0
            visited.pop()
            idx.pop()

for d in range(1, N + 1):
    dfs(0, S, d)

print(cnt)