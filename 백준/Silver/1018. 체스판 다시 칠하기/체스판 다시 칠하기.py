M,N = map(int,input().split()) # M 행 / N 열
board = [input() for row in range(M)]
# print(board)

# chess 인자 : board에서 8 x 8 영역로 가져옴.
# topleft 인자 : 8x8 chess판의 가장 왼쪽이 W로 시작하는지 B로 시작하는지 기준 설정
 
def f(chess,topleft):
    cnt = 0
    # topleft 가 B인 경우
    # BWBWBWBW 0행 - 0열, 2열, 4열, 6열(B) / 1열, 3열, 5열, 7열(W)
    # WBWBWBWB 1행 - 
    for i in range(0,8,2): # 0행 2행 4행 6행 B이 시작
        for j in range(0,8,2): # 0열 2열 4열 6열 6열 B
            if chess[i][j] == topleft: # B이면 넘어가!
                continue
            if chess[i][j] != topleft: # W으면 칠해!
                cnt += 1
        for j in range(1,8,2): # 1열 3열 5열 7열 W
            if chess[i][j] != topleft: # 1 3 5 7열 W면 넘어가!
                continue
            if chess[i][j] == topleft: # B이면 칠해!
                cnt += 1
    for i in range(1,8,2): # 1행 3행 5행 7행 W가 시작
        for j in range(0,8,2): # 0열 2열 4열 6열 6열 W
            if chess[i][j] != topleft: # W시작이니까 W면 넘어가
                continue
            if chess[i][j] == topleft: # W시작이니까 B이면 칠해 
                cnt += 1
        for j in range(1,8,2): # 1열 3열 5열 7열 B
            if chess[i][j] == topleft: 
                continue
            if chess[i][j] != topleft:
                cnt += 1
        
    return cnt

cnt = 2500 # 임의의 큰 수

for j in range(N-7):
    for i in range(M-7):
        chess =[]
        for z in range(i,i+8):
            chess.append(board[z][j:j+8])
        cnt = min(cnt, f(chess, 'B'), f(chess, 'W'))
        
print(cnt)