N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

def solution(N, points):
    MAX_X = int(1e5) + 1
    
    x_cnt = [0] * MAX_X
    y_cnt = [0] * MAX_X
    
    for x, y in points:
        x_cnt[x] += 1
        y_cnt[y] += 1
        
    cnt = 0
    for x, y in points:
        if x_cnt[x] >= 2 and y_cnt[y] >= 2:
            cnt += (x_cnt[x] - 1) * (y_cnt[y] - 1)
            
    return cnt

print(solution(N, points))