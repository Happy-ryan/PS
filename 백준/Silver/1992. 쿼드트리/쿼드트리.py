n = int(input())
board = [list(input()) for _ in range(n)]

def solution(n, board):
    global ans
    def check(r, c, dr, dc):   
            flag = board[r][c]
            for i in range(r, r + dr):
                for j in range(c, c + dc):
                    if board[i][j] != flag:
                        return False
            return flag
    
    ans = ''
    def f(r, c, x, y):
        global ans
        # 재귀는 종료조건!
        flag = check(r, c, x, y)
        if flag:
            ans += flag
            return
        
        ans += '('
        # 절반씩 보자
        f(r, c, x // 2, y // 2)
        f(r, c + y // 2, x // 2, y // 2)
        f(r + x // 2, c, x // 2, y // 2)
        f(r + x // 2, c + y // 2, x // 2, y // 2)
        ans += ')'
    
    # 재귀
    f(0, 0, n, n)
    
    return ans
    
print(solution(n, board))