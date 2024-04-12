# https://www.acmicpc.net/problem/19238

n, m, init_fuel_quantity = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cr, cc = map(int, input().split())
cr -= 1
cc -= 1
customers = [list(map(int, input().split())) for _ in range(m)]
for idx in range(m):
    for x in range(4):
        customers[idx][x] -= 1

# 1. 현재의 택시 위치에서 가장 가까운 거리의 승객에게 이동한다.
# 1-1. bfs - dist 활용
# 1-2. 최단거리가 동일한 경우 행 번호가 작은 승객 먼저 > 같다면 열번호가 작은 승객 먼저
# 1-3. 택시와 승객이 같은 위치에 있으면 승객까지의 최단거리 0

from collections import deque


def solution(n, m, init_fuel_quantity, board, cr, cc, customers):
    inf = int(1e18)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n

    def bfs(r, c):
        visited = [[False for _ in range(n)] for _ in range(n)]
        dist = [[inf for _ in range(n)] for _ in range(n)]

        dq = deque([])
        dq.append((r, c))
        visited[r][c] = True
        dist[r][c] = 0

        while dq:
            cr, cc = dq.popleft()
            for k in range(4):
                nr = cr + dr[k]
                nc = cc + dc[k]
                if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 0:
                    dq.append((nr, nc))
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[cr][cc] + 1

        return dist

    # 방문한 고객은 방문하지않도록
    memo = []

    def decide_customer(r, c, cur_fuel, customers):
        dist = bfs(r, c)
        # 연료, 행번호, 열번호 (작은 것!)
        min_dist_customer = (inf, inf, inf, inf)
        for idx, row in enumerate(customers):
            # 이미 방문한 고객 번호면 넘어가자
            if idx in memo:
                continue
            customer_r, customer_c, _, _ = row
            if cur_fuel >= dist[customer_r][customer_c]:
                min_dist_customer = min(
                    min_dist_customer,
                    (dist[customer_r][customer_c], customer_r, customer_c, idx),
                )
                # print(min_dist_customer)

        # 택시위치 > 승객 소모되는 fuel, r, c, idx(고객번호)
        return min_dist_customer

    def move(cur_fuel, idx):
        sr, sc, er, ec = customers[idx]
        # (4, 3) (0, 5) - L1거리
        # (0, 0) ~ (0, 5) 까지 소모되는 연료의 양은? 5 (0 - 0 + 5 - 0)
        # (1, 1) ~ (2, 6) 까지 소모되는 연료의 양은? 7 (2 - 1 + 6 - 1) = 6
        
        # 이동할 수 없는 곳인데 좌표 이용해서 연료소모량을 계산했기에 틀려버림!!! < 틀린이유
        dist = bfs(sr, sc)
        used_fuel = dist[er][ec]
        if cur_fuel < used_fuel:
            return inf, inf, inf
        # (소모량의 2배 충전, 목적지 행, 목적지 열)
        # 2배를 충전해준다는 것은 승객을 태우는 동안은 연료 소모가 안되는 것과 동일한 상황인 것이다.
        return used_fuel, er, ec

    # 고객 다 태울 수 있는데까지 최대한 하자!
    ans = 0
    while len(memo) != m:
        # (승객에게 가는데 걸리는 량, 승객의 위치(r), 승객의 위치(c), 승객의 번호)
        # print(f"택시의 초기위치: {cr}, {cc} | 초기 연료량: {init_fuel_quantity}")
        move_fuel, r, c, idx = decide_customer(cr, cc, init_fuel_quantity, customers)
        # print(
        #     f"고객의 출발지 위치: {r}, {c} | 번호:  {idx} | 이동 연료량: {move_fuel} | 현재 누적 연료량: {init_fuel_quantity - move_fuel}"
        # )
        memo.append(idx)
        if move_fuel >= inf:
            return -1
        # 이동 후 소모된 연료의 양
        cur_fuel = init_fuel_quantity - move_fuel

        charge_fuel, er, ec = move(cur_fuel, idx)
        if charge_fuel >= inf:
            ans = inf
            return -1
        # print(
        #     f"고객의 도착지 위치: {er}, {ec} | 번호:  {idx} | 소모 연료량: {charge_fuel} | 충전 후 누적 연료량: {cur_fuel + charge_fuel}"
        # )

        # 위치 초기화
        cr, cc, init_fuel_quantity = er, ec, cur_fuel + charge_fuel
        # print("=")

    ans = init_fuel_quantity
    return ans


print(solution(n, m, init_fuel_quantity, board, cr, cc, customers))