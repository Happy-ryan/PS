n, m = map(int, input().split())
cmds = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, cmds):
    arr = list(range(1, n + 1))
    
    for cmd in cmds:
        i, j = cmd
        i -= 1
        j -= 1
        p1 = arr[:i]
        p2 = arr[i:j + 1][::-1]
        p3 = arr[j + 1:]
        arr = p1 + p2 + p3

    return arr
        
print(*solution(n, m, cmds))