# https://www.acmicpc.net/problem/15664

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = set()
visted = []
used = [0] * n


def dfs(level, m):
    if level == m:
        row = visted.copy()
        if row == sorted(row) and tuple(row) not in ans:
            ans.add(tuple(row))
            print(*row)
        return

    for idx, num in enumerate(nums):
        if not used[idx]:
            visted.append(num)
            used[idx] = 1
            dfs(level + 1, m)
            visted.pop()
            used[idx] = 0


dfs(0, m)