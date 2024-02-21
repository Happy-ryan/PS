from collections import deque

n, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 1번. 국경에 대한 판단이 필요하다! > 그룹 찾기
def bfs(r, c, in_queue):
    dq = deque([])
    dq.append((r, c))
    in_queue[r][c] = True
    people = [(r, c, board[r][c])]
    
    
    while dq:
        cr, cc = dq.popleft()
        # print(f"1 - cc: {cc}, cr: {cr}")
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            # print(f"2 - nr: {nr}, nc: {nc}")
            if in_range(nr, nc) and not in_queue[nr][nc] and L <= abs(board[nr][nc] - board[cr][cc]) <= R:
                # print(f"3 - nr: {nr}, nc: {nc}")
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                people.append((nr, nc, board[nr][nc]))
                
    return people

def simulate():
    in_queue = [[False for _ in range(n)] for _ in range(n)]
    
    people_list = []
    for r in range(n):
        for c in range(n):
            if in_queue[r][c]:
                continue
            people_list.append(bfs(r, c, in_queue))
    
    if len(people_list) == n ** 2:
        return False

    for people in people_list:
        sum_val = 0
        for person in people:
            sum_val += person[2]
        avg = sum_val // len(people)
        for person in people:
            board[person[0]][person[1]] = avg
            
    return True
            

t = 0
while True:
    if not simulate():
        print(t)
        break
    t += 1