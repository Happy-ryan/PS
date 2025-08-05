n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

from collections import deque

def solution(n, m, board):
    
    def get_init(x):
        for i in range(n):
            for j in range(m):
                if x == board[i][j]:
                    return (i, j)
    
    def move_right(r, c):
        for i in range(c, m):
            if board[r][i] == '.':
                c = i
                continue
            if board[r][i] == '#':
                c = i -1
                break
            if board[r][i] == 'O':
                c = i
                break
        return r, c

    def move_left(r, c):
        for i in reversed(range(c)):
            if board[r][i] == '.':
                c = i
                continue
            if board[r][i] == '#':
                c = i + 1
                break
            if board[r][i] == 'O':
                c = i
                break
        return r, c

    def move_up(r, c):
        for i in reversed(range(r)):
            if board[i][c] == '.':
                r = i
                continue
            if board[i][c] == '#':
                r = i + 1
                break
            if board[i][c] == 'O':
                r = i
                break
        return r, c

    def move_down(r, c):
        for i in range(r, n):
            if board[i][c] == '.':
                r = i
                continue
            if board[i][c] == '#':
                r = i - 1
                break
            if board[i][c] == 'O':
                r = i
                break
        return r, c

    
    def go_right(rr, rc, br, bc):
        nrr, nrc = move_right(rr, rc)
        nbr, nbc = move_right(br, bc)
        if (nrr, nrc) == (nbr, nbc): # 공이 같은 자리에 있을 때
            if (nrr, nrc) == blank: # 공이 동시에 구멍에 빠진 상황: 금지된 상황
                return (-1, -1, -1, -1)
            # 공이 겹친상황: 보정이 필요
            if rc < bc:
                nrc -= 1
            elif rc > bc:
                nbc -= 1
        return nrr, nrc, nbr, nbc
    
    def go_left(rr, rc, br, bc):
        nrr, nrc = move_left(rr, rc)
        nbr, nbc = move_left(br, bc)
        if (nrr, nrc) == (nbr, nbc): # 공이 같은 자리에 있을 때
            if (nrr, nrc) == blank: # 공이 동시에 구멍에 빠진 상황: 금지된 상황
                return (-1, -1, -1, -1)
            # 공이 겹친상황: 보정이 필요
            if rc < bc: # R 1, B 4 -> R 1, B 1 -> R 1, B 2
                nbc += 1
            elif rc > bc:
                nrc += 1
        return nrr, nrc, nbr, nbc
    
    def go_up(rr, rc, br, bc):
        nrr, nrc = move_up(rr, rc)
        nbr, nbc = move_up(br, bc)
        if (nrr, nrc) == (nbr, nbc): # 공이 같은 자리에 있을 때
            if (nrr, nrc) == blank: # 공이 동시에 구멍에 빠진 상황: 금지된 상황
                return (-1, -1, -1, -1)
            # 공이 겹친상황: 보정이 필요
            if rr < br:
                nbr += 1
            elif rr > br:
                nrr += 1
        return nrr, nrc, nbr, nbc
    
    def go_down(rr, rc, br, bc):
        nrr, nrc = move_down(rr, rc)
        nbr, nbc = move_down(br, bc)
        if (nrr, nrc) == (nbr, nbc): # 공이 같은 자리에 있을 때
            if (nrr, nrc) == blank: # 공이 동시에 구멍에 빠진 상황: 금지된 상황
                return (-1, -1, -1, -1)
            # 공이 겹친상황: 보정이 필요
            if rr < br:
                nrr -= 1
            elif rr > br:
                nbr -= 1
        return nrr, nrc, nbr, nbc
    
    def process(rr, rc, br, bc, dir):
        if dir == 0:
            return go_right(rr, rc, br, bc)
        if dir == 1:
            return go_down(rr, rc, br, bc)
        if dir == 2:
            return go_left(rr, rc, br, bc)
        if dir == 3:
            return go_up(rr, rc, br, bc)
        
    
    red, blue, blank = get_init('R'), get_init('B'), get_init('O')
    
    board[red[0]][red[1]] = '.'
    board[blue[0]][blue[1]] = '.'
    
    def bfs():
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        def in_range(r, c):
            return 0 <= r < n and 0 <= c < m 
        
        
        # (m -> n) -> m -> n
        # c2    r2    c1   r1
        in_queue = [
                    [
                    [[False for _ in range(m)] for _ in range(n)]
                    for _ in range(m)
                    ]
                    for _ in range(n)
                    ]
        inf = int(1e18)
        # 초기상태 (r1, c1) (r2, c2) -> 다음 상태 (nr1, nc1) (nr2, nc2) 까지의 최단거리 = dist[nr1][nc1][nr2][nc2]
        dist = [
                [
                [[inf for _ in range(m)] for _ in range(n)]
                for _ in range(m)
                ]
                for _ in range(n)
                ]
        
        dq = deque([])
        r1, c1, r2, c2 = red[0], red[1], blue[0], blue[1]
        dq.append((r1, c1, r2, c2))
        in_queue[r1][c1][r2][c2] = True
        dist[r1][c1][r2][c2] = 0
        
        while dq:
            rr, rc, br, bc = dq.popleft()
            
            # print(f"d: {d}, rr: {rr}, rc: {rc}, br: {br}, bc: {bc}")
            
            cur_dist = dist[rr][rc][br][bc]
            
            if cur_dist > 10:
                return -1
            
            if (rr, rc) == blank:
                return dist[rr][rc][br][bc]
            
            for k in range(4):
                nrr, nrc, nbr, nbc = process(rr, rc, br, bc, k)
                # print(f"process({rr}, {rc}, {br}, {bc}) = ", k, nrr, nrc, nbr, nbc)
                if (nbr, nbc) == blank:
                    continue
                if in_range(nrr, nrc) and in_range(nbr, nbc) and not in_queue[nrr][nrc][nbr][nbc]:
                    dq.append((nrr, nrc, nbr, nbc))
                    in_queue[nrr][nrc][nbr][nbc] = True
                    dist[nrr][nrc][nbr][nbc] = cur_dist + 1
            
        return -1

    res = bfs()
    
    return res

    
    
print(solution(n, m, board))