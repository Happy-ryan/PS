n = int(input())
w = 2**n
board = [[" " for _ in range(w)] for _ in range(w)]
# w 일 때 (0, 0), (0, w), (w, 0) 
def f(x, r, c):
    # 종료조건
    if x == 0:
        board[r][c] = "*"
        return
    # 직각 꼭지점의 좌표 (r, c) (r, c + 한 변의 길이), (r + 한 변의 길이, c)
    # w는 고정된 값...변의 길이는 고정된 값이 아니라 재귀를 돌 때마다 갱신되어야함.
    
    d = 2 ** x // 2
    
    f(x - 1, r, c)
    f(x - 1, r + d, c)
    f(x - 1, r, c + d)
    
f(n, 0, 0)

ans = []
for row in board:
    for idx in range(len(row) - 1, -1, -1):
        if row[idx] != ' ':
            ans.append(row[:idx + 1])
            break

for row in ans:
    print(*row, sep="")