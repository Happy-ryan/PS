t = int(input())

def solution(n, m):

    cnt = 2 * m - n
    
    return [cnt, m - cnt]

for _ in range(t):
    n, m = map(int, input().split())
    print(*solution(n, m))