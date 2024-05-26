n, x, k = map(int, input().split())
cmds = [list(map(int, input().split())) for _ in range(k)]


def solution(n, x, k, cmds):
    
    memo = [0] * (n + 1)
    memo[x] = 1
    
    for cmd in cmds:
        a, b = cmd
        memo[a], memo[b] = memo[b], memo[a]
        
    return memo.index(1)


print(solution(n, x, k, cmds))