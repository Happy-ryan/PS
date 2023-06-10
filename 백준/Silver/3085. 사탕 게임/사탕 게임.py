# https://www.acmicpc.net/problem/3085
# 시간복잡도: 4*N^2*2N = O(N^2)

# -- 연속된 문자열 갯수 체크하는 함수
def custom_split(s: str or list):
    continus_cnt = []
    previous = s[0]
    cnt = 1
    for x in s[1:]:
        if x == previous:
            cnt += 1
        else:
            continus_cnt.append(cnt)
            cnt = 1  # 다시 초기화
            previous = x  # 바뀐걸로 previous 초기화
    continus_cnt.append(cnt)
    return max(continus_cnt)


def bomb(r, c, board):
    n = len(board)
    row = "".join(board[r])
    col = ""
    for i in range(n):
        col += board[i][c]

    return max(custom_split(row), custom_split(col))


def check(r, c, board):
    n = len(board)
    return 0 <= r < n and 0 <= c < n


def solution(origin_board):
    board = []
    for row in origin_board:
        board.append(list(row))
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    for r in range(len(board)):
        for c in range(len(board)):
            for k in range(4):
                # new_board = deepcopy(board)
                nr, nc = r + dr[k], c + dc[k]
                if check(nr, nc, board):
                    # -- 바꾸기
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]
                    ans = max(ans, bomb(r, c, board))
                    # -- 원상복귀
                    board[r][c], board[nr][nc] = board[nr][nc], board[r][c]

    return ans


n = int(input())
board = [input() for row in range(n)]
print(solution(board))
