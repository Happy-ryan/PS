n = int(input())
board = [list(input()) for _ in range(n)]

def solution(n, board):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 1. 심장의 위치
    # 심장만 4방향(상, 하, 좌, 우)에 모두 신체부위가 존재.
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    
    def find_heart():
        for r in range(n):
            for c in range(n):
                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if in_range(nr, nc) and board[nr][nc] == '*':
                        cnt += 1
                if cnt == 4:
                    return (r, c)
            
    h_r, h_c = find_heart()
    # 왼쪽, 오른쪽 팔 : 심장으로부터 좌/우 마지막 '*'까지 확인
    def cal_arm(mode, h_r, h_c):
        cnt = 0
        if mode == 'r':
            for c in range(h_c + 1, n):
                if board[h_r][c] == '*':
                    cnt += 1
        else:
            for c in range(0, h_c):
                if board[h_r][c] == '*':
                    cnt += 1
        return cnt
    # 허리 : 심장으로부터 하 마지막 '*'까지 확인
    def cal_her(h_r, h_c):
        cnt = 0
        for r in range(h_r + 1, n):
            if board[r][h_c] == '*':
                cnt += 1
        return cnt
    # 다리 길이 : 허리 마지막 위치에서 좌/우 대각선 -> 이후 마지막 '*'까지 확인
    def cal_leg(mode, h_r, h_c, heri):
        heri_r, heri_c = h_r + heri, h_c
        cnt = 0
        if mode == 'r':
            leg_r, leg_c = (heri_r + 1, heri_c + 1)
            for r in range(leg_r, n):
                if board[r][leg_c] == '*':
                    cnt += 1
        else:
            leg_r, leg_c = (heri_r + 1, heri_c - 1)
            for r in range(leg_r, n):
                if board[r][leg_c] == '*':
                    cnt += 1
                    
        return cnt
            
    # print(f"심장 위치 : {h_r}, {h_c}")
    # print(f"왼팔 길이 : {cal_arm('l', h_r, h_c)}")
    # print(f"오른팔 길이 : {cal_arm('r', h_r, h_c)}")
    # print(f"허리 길이 : {cal_her(h_r, h_c)}")
    # print(f"왼다리 길이 : {cal_leg('l', h_r, h_c, cal_her(h_r, h_c))}")
    # print(f"오른다리 길이 : {cal_leg('r', h_r, h_c, cal_her(h_r, h_c))}")
    print(h_r + 1, h_c + 1)
    left_arm, right_arm = cal_arm('l', h_r, h_c), cal_arm('r', h_r, h_c)
    heri = cal_her(h_r, h_c)
    left_leg, right_leg = cal_leg('l', h_r, h_c, heri), cal_leg('r', h_r, h_c, heri)
    print(left_arm, right_arm, heri, left_leg, right_leg)
            

solution(n, board)