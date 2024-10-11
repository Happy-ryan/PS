n = int(input())
difficulty_levels = [int(input()) for _ in range(n)]

def solution(n, difficulty_levels):
    # 난이도 하위15% 상위15% 제거
    # 쉽게 제거하기 위해서 정렬
    difficulty_levels.sort()
    
    inf = 1e-9
    
    if n == 0:
        return 0
    
    # 반올림
    x = int(round(n * 0.15 +inf, 0))
    cnt = 0
    sum_val = inf
    for idx in range(x, n - x):
        sum_val += difficulty_levels[idx]
        cnt += 1
    
    return int(round(sum_val / cnt, 0))
    
print(solution(n, difficulty_levels))