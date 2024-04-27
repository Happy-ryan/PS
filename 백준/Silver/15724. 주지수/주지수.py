# https://www.acmicpc.net/problem/15724

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
t = int(input())
tests = [list(map(int, input().split())) for _ in range(t)]

# 누적합 중 RangeSum 문제이다.
def solution(n, m, board, tests):
    answer = []
    # 2차원 누적합 문제
    psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for r in range(n):
        for c in range(m):
            psum[r + 1][c + 1] = board[r][c] + psum[r + 1][c] + psum[r][c + 1] - psum[r][c]
            
    # for row in psum:
    #     print(row)
            
    for test in tests:
        # 1base
        r1, c1, r2, c2 = test
        rangeSum = psum[r2][c2] - psum[r1 - 1][c2] - psum[r2][c1 - 1] + psum[r1 - 1][c1 - 1]
        print(rangeSum)
        
        
solution(n, m, board, tests)