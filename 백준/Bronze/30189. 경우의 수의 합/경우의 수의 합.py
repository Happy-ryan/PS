n, m = map(int, input().split())

def solution(n, m):
    
    # 시간복잡도 N * M 
    def f(c):
        cnt = 0
        for x in range(n + 1):
            for y in range(m + 1):
                if x + y == c:
                    cnt += 1
        return cnt
    # 시간복잡도 N + M
    
    # 최종 (N + M)(N * M) = (100 + 100) * (100 * 100) = 200 * 10000 = 2000000
    cnt = 0
    for c in range(n + m + 1):
        cnt += f(c)
    
    return cnt

print(solution(n, m))