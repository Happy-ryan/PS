n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def solution(n, board):
    inf = int(1e18)
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    def make_psum_2d():
        psum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        
        for r in range(n):
            for c in range(n):
                psum[r + 1][c + 1] = board[r][c] + psum[r + 1][c] + psum[r][c + 1] - psum[r][c]
        
        return psum
    
    def range_sum(psum, r1, c1, r2, c2):
        return psum[r2 + 1][c2 + 1] - psum[r2 + 1][c1] - psum[r1][c2 + 1] + psum[r1][c1]
    
    psum = make_psum_2d()
    # for row in psum:
    #     print(row)
    
    # 정사각형 모양으로만 가져갈 수 있음
    # 왼쪽 상단 고정 <- for문 2번
    # 길이 1 <= k < n <- 길이 for문 1번
    # 300 * 300 * 300 = 9000000 > 브루트포스 가능!
    max_ans = -inf
    for l_r in range(n):
        for l_c in range(n):
            # 기본적으로 1x1칸이다. 따라서 k = 0 이면 1칸을 의미함.
            for k in range(n):
                r_r = l_r + k
                r_c = l_c + k
                if in_range(r_r, r_c):
                    # print(f"l_r: {l_r}, l_c: {l_c}, r_r: {r_r}, r_c: {r_c}, 한 변의 길이: {k + 1}, sum: {range_sum(psum, l_r, l_c, r_r, r_c)}")
                    max_ans = max(max_ans, range_sum(psum, l_r, l_c, r_r, r_c))
                    
    
    return max_ans

print(solution(n, board))