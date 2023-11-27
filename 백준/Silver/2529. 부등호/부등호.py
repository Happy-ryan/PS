# https://www.acmicpc.net/problem/2529

n = int(input())
cmds = list(input().split())


def listToInt(row: list[int]):
    ans = 0
    for digit in row:
        ans *= 10
        ans += digit
    return ans


def check(cmds: list[str], nums: list[int]):
    for idx in range(1, len(nums)):
        if cmds[idx - 1] == "<" and nums[idx - 1] < nums[idx]:
            continue
        elif cmds[idx - 1] == ">" and nums[idx - 1] > nums[idx]:
            continue
        else:
            return False
    return True


visited = []
used = [0] * 10

inf = int(1e10)
max_num = -inf
min_num = inf


def dfs(level, n):
    global max_num, min_num
    if level == n:
        nums = visited.copy()
        if check(cmds, nums):
            max_num = max(max_num, listToInt(nums))
            min_num = min(min_num, listToInt(nums))
        return

    for i in range(10):
        if not used[i]:
            visited.append(i)
            used[i] = 1
            dfs(level + 1, n)
            visited.pop()
            used[i] = 0


dfs(0, n + 1)

print(max_num)

print("0" * (n + 1 - len(str(min_num))) + str(min_num))