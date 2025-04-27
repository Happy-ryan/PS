n = int(input())
memo = list(map(int, input().split()))
records = [list(map(int, input().split())) for _ in range(n)]

def solution(n, memo, records):
    ans = 0
    for i in range(n):
        x, y = records[i]
        if memo[i] == 1 and y - x >= 0:
            ans += y - x
    
    return ans

print(solution(n, memo, records))