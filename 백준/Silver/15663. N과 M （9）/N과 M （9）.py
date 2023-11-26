# https://www.acmicpc.net/problem/15663

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = set()
visted = []
used = [0] * n


def dfs(level, m):
    if level == m:
        # TypeError: unhashable type: 'list' 에러 발생
        # immutable -> hashable -> list=> tuple 
        row = tuple(visted.copy())
        if row not in set(ans):
            ans.add(row)
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