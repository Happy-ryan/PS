n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
qs = [list(map(int, input().split())) for _ in range(k)]

def solution(n, m, board, qs):
    psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    # 1. 누적합
    def make_psum():
        # 0base board -> 1base psum
        for i in range(n):
            for j in range(m):
                psum[i + 1][j + 1] = board[i][j] + psum[i][j + 1] + psum[i + 1][j] - psum[i][j]
                
    make_psum()
    # 0base board -> 1base psum : psum[i + 1][j + 1] = b[i][j] + psum[]
    # for row in psum:
    #     print(row)
        
    # 2. 출력
    def cal(r1, c1, r2, c2):
        # psum, r1, c1, r2, c2 1base
        return psum[r2][c2] - psum[r2][c1 - 1] - psum[r1 - 1][c2] + psum[r1 - 1][c1 - 1]
    
    for i, j, x, y in qs:
        print(cal(i, j, x, y))
        
solution(n, m, board, qs)