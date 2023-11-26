def dfs(level, start, path):
    if level == m:
        print(*path)
        return

    for i in range(start, n):
        if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
            continue

        visited.append(nums[i])
        used[i] = 1
        dfs(level + 1, i + 1, path + [nums[i]])
        visited.pop()
        used[i] = 0


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = set()
visited = []
used = [0] * n

dfs(0, 0, [])
