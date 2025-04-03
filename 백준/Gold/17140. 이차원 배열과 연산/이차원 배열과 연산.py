# 정렬순서
# 1. 등장횟수가 커지는 순서로 페어, 오름차순
# 2. 등장횟수가 동일하면 숫자가 커지는 순으로 페어, 오름차순

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

from collections import Counter
from copy import deepcopy

def solution(r, c, k, board):
    
    # 정렬 연산
    def array_rc(rc: list[int]):
        dic = Counter(rc)
        tmp = []
        for k, v in dic.items():
            if k != 0:    
                tmp.append((k, v))
        
        tmp.sort(key= lambda x: (x[1], x[0]))
        
        ans = []
        
        for k, v in tmp:
            ans.append(k)
            ans.append(v)
        
        return ans[:100] # 100 넘는건 삭제
    
    # R연산
    def R_f():
        max_row = 0
        tmp = []
        for row in board:
            tmp_row = array_rc(row)
            tmp.append(tmp_row)
            max_row = max(max_row, len(tmp_row))

        ans = []
        for t in tmp:
            if len(t) < max_row:
                t += [0] * (max_row - len(t))
            ans.append(t)
        
        return ans
    
    # C연산
    def C_f():
        max_col = 0
        # 정렬하기 위해 열 뽑는 로직
        R, C = len(board), len(board[0])
        tmp = []
        for j in range(C):
            tmp_col = []
            for i in range(R):
                tmp_col.append(board[i][j])

            
            tmp_new_col = array_rc(tmp_col)
            tmp.append(tmp_new_col)
            max_col = max(max_col, len(tmp_new_col))
        # 각 배열 정렬 후 모음
        tmp2 = []
        for t in tmp:
            if len(t) < max_col:
                t += [0] * (max_col - len(t))
            tmp2.append(t)
        
        # C연산의 경우, 배열을 다시 열로 변경해줘야함.
        tmp_r, tmp_c = len(tmp2), len(tmp2[0])
        R, C = tmp_c, tmp_r
        ans = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(tmp_r):
            for j in range(tmp_c):
                    ans[j][i] = tmp2[i][j]
            
        return ans
    
    t = 0
    while True:
        if t > 100:
            return -1
        # board가 커지기 전에는 index error 발생
        R, C = len(board), len(board[0])
        if R >= r and C >= c and board[r - 1][c - 1] == k:
            return t
        # print(f"========{t}초 : 연산 전========")
        # for row in board:
        #     print(*row)
        if R >= C:
            board = R_f()
            # print(">>>>>>>>>>>R 연산 중....>>>>>>>>>>>")
        else:
            board = C_f()
            # print(">>>>>>>>>>>C 연산 중....>>>>>>>>>>>")
        t += 1
        # print(f"========{t}초 : 연산 후========")
        # for row in board:
        #     print(*row)
    
print(solution(r, c, k, board))
