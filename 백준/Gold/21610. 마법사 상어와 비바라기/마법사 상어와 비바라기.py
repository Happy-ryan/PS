n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
Ms = [list(map(int, input().split())) for _ in range(m)]

from copy import deepcopy
from collections import Counter

def solution(n, m, board, Ms):
    # 바구니 : 저장할 수 있는 물의 양 제한 없음
    # A[r][c] = 바구니에 저장되어 있는 물의 양

    #  최초 비구름 위치 (N, 1), (N, 2), (N-1, 1), (N-1, 2) <- 1base
    clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
    water_areas = []
    
    # 구름 이동 M번 - 방향(di) / 거리(si)
    # 8개의 방향으로 이루어짐.
    
    # d_i, s_i > 1 ~ 5 거치고 구름이 생성
    # d_i+1 s_i+1 > 1 ~ 5 거친다...
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    #1. 모든 구름이 di 방향으로 si칸 이동한다.
    def move(d, s):
        nonlocal clouds
        # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
        dr = [0, -1, -1, -1, 0, 1, 1, 1]
        dc = [-1, -1, 0, 1, 1, 1, 0, -1]
        new_clouds = []
        for cloud in clouds:
            nr = (cloud[0] + dr[d] * s) % n
            nc = (cloud[1] + dc[d] * s) % n
            new_clouds.append((nr, nc))
            
        # 구름 위치 갱신!
        clouds = deepcopy(new_clouds)
    
    #2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    def rain():
        for cloud in clouds:
            r, c = cloud
            board[r][c] += 1
    #3. 구름이 모두 사라진다.
    def clean_clouds():
        nonlocal clouds, water_areas
        water_areas = deepcopy(clouds)
        clouds = []
    # 4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
    # 4-1.이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    # 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
    def magic():
        dr_m = [-1, -1, 1, 1]
        dc_m = [1, -1, 1, -1]
        dic = Counter()
        for area in water_areas:
            dic[area] = board[area[0]][area[1]]
        
        
        for area in dic.keys():
            cr, cc = area
            cnt = 0
            for k in range(4):
                nr = cr + dr_m[k]
                nc = cc + dc_m[k]
                if in_range(nr, nc) and board[nr][nc] != 0:
                    cnt += 1
            dic[area] += cnt
            
        for area, value in dic.items():
            r, c = area
            board[r][c] = value
    
    
    #5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    def create_clouds():
        nonlocal water_areas, clouds
        for r in range(n):
            for c in range(n):
                if board[r][c] >= 2 and (r, c) not in water_areas:
                    clouds.append((r, c))
                    board[r][c] -= 2
        water_areas = []
        
    for (d, s) in Ms:
        # print("구름 이동 전 위치...")
        # print(clouds)
        move(d - 1, s)
        # print("구름 이동 후 위치...")
        # print(clouds)
        # print("비 내리기 전 상황...")
        # for row in board:
        #     print(*row)
        rain()
        # print("비 내린 후 상황...")
        # for row in board:
        #     print(*row)
        # print("====!!구름 삭제!!====")
        clean_clouds()
        # print("비 내린 지역")
        # print(water_areas)
        # print("구름의 상태")
        # print(clouds)
        # print("====!!매직 시도!!===")
        magic()
        # print("매직 시도 완료...")
        # for row in board:
        #     print(*row)
        # print("구름 생성....")
        create_clouds()
        # print("비 내린 지역")
        # print(water_areas)
        # print("구름의 상태")
        # print(clouds)
        # print("구름 생성 후 상황...")
        # for row in board:
        #     print(*row)
        # print("=====한 번 끝=====")
    
    sum_val = 0
    for row in board:
        sum_val += sum(row)
        
    return sum_val

print(solution(n, m, board, Ms))