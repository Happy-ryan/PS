n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

# 모든 행과 모든 열에 한 명 이상의 경비원 존재
# 몇 명의 경비원을 최소로 추가해야하는가?

def solution(n, m, board):
    
    def row_check():
        cnt = 0
        for row in board:
            if 'X' not in row:
                cnt += 1
        return cnt
    
    def col_check():
        cnt = 0
        for c in range(m):
            flag = False
            for r in range(n):
                if board[r][c] == 'X':
                    flag = True
            if not flag:
                cnt += 1
        return cnt
    
    return max(row_check(), col_check())

print(solution(n, m, board))