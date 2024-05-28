t = int(input())
arr = [input() for _ in range(t)]

def solution(t, arr):
    inf = int(1e18)
    cnt = -inf
    for row in arr:
        cnt = max(cnt, row.count('for') + row.count('while'))
        
    return cnt

print(solution(t, arr))