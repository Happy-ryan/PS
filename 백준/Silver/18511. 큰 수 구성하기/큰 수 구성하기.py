n, k = map(int, input().split())
nums = list(map(int, input().split()))
visited = []


def dfs(level, depth):
    best_num = 0
    if level == depth:
        return int(''.join(map(str, visited)))
    for i in range(k):
        visited.append(nums[i])
        num = dfs(level + 1, depth)
        if num is not None and num <= n:
            best_num = max(num, best_num)
        visited.pop()
    return best_num
    
print(max([dfs(0, i) for i in range(1, len(str(n)) + 1)]))