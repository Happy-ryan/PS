n, m = map(int, input().split())
highs = list(map(int, input().split()))
cmds = [list(map(int, input().split())) for _ in range(m)]


def solution(n, m, highs, cmds):
    answer = [0] * n
    nums = [0] * (n + 1)
    for cmd in cmds:
        a, b, k = cmd
        nums[a - 1] += k
        nums[b] -= k


    for i in range(n - 1):
        nums[i + 1] += nums[i]

    for i in range(n):
        highs[i] += nums[i]
        
    return highs


print(*solution(n, m, highs, cmds))