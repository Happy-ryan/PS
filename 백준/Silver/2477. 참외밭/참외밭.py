k = int(input())
grids = [list(map(int, input().split())) for _ in range(6)]

def solution(k, grids):
    max_n = 505
    
    N = 6 # 다각형
    
    cx, cy = max_n, max_n
    
    arr = []
    for grid in grids:
        dir, val = grid
        if dir == 1:
            cx -= val
        elif dir == 2:
            cx += val
        elif dir == 3:
            cy -= val
        else:
            cy += val
        arr.append((cx, cy))
    
    # 사선공식 활용을 위해 닫기
    arr.append(arr[0])
    
    # 반시계방향으로 주어지기때문에 사선공식 가능
    def cal(grids):
        sum_val1, sum_val2 = 0, 0
        for x in range(N):
            sum_val1 += grids[x][0] * grids[x + 1][1]
            sum_val2 += grids[x][1] * grids[x + 1][0]
        
        return 0.5 * abs(sum_val1 - sum_val2)

    return f"{cal(arr) * k:.0f}"
    
print(solution(k, grids))