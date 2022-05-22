N = int(input())
w = 4*N - 3 # 규칙찾기
# 1>1 // 2>>5 // 3>>9 // 4>>13 +4등차수열 : 4*n - 3
board =[[" "for _ in range(w)] for _ in range(w)] # list comprehension
# #pprint(board)

def f(w,x,y,board) : #규칙에 맞는 사각형을 그리는 함수 # 별을 넣을 판을 먼저 깔아야한다.
    if w < 0 : return # 재귀함수의 바닥역할, 애초에 W는 한 변의 길이이므로 반드시 >0 야 한다.
    # 위 가로 (0,0)~(0,w) // 밑 가로(w-1,0)~(w-1,w-1) 10~12 line
    for i in range(w):
        board[x][y+i] = "*"
        board[x+w-1][y+i] ="*"
    for j in range(1,w-1):
        board[x+j][y] ="*"
        board[x+j][y+w-1] ="*"
    f(w-4, x+2, y+2,board)
f(w,0,0,board)

for row in board:
    print(*row,sep="")