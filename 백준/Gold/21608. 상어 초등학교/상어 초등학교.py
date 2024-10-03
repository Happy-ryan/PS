n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]

from collections import defaultdict
def solution(n, students):
    # 
    students_infos = defaultdict(list)
    for row in students:
        students_infos[row[0]] = row[1:]
    # 인접하는 칸: |r1 - r2| + |c1 - c2| = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 칸
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n
    
    # 1.비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    # 3.2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    def choose(student_number, student_prefer):
        candidate_seat = []
        for r in range(n):
            for c in range(n):
                pref_cnt = 0
                blank_cnt = 0
                # 해당 칸 비어있음!
                if board[r][c] == 0:
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if in_range(nr, nc):
                            if board[nr][nc] in students_infos[student_number]:
                                pref_cnt += 1
                            if board[nr][nc] == 0:
                                blank_cnt += 1
                    candidate_seat.append((pref_cnt, blank_cnt, r, c))
                    # print(f"학생 번호: {student_number}, 인접한 칸의 선호학생의 수: {pref_cnt}, 인접한 칸의 빈칸의 수: {blank_cnt}, 좌표: {(r, c)}")
        # (r, c) 기준 인접한 칸의 선호학생의 수, (r, c) 기준 인접한 칸의 빈칸의 수, 행, 열
        candidate_seat.sort(key=lambda x : (-x[0], -x[1], x[2], x[3]))
        return candidate_seat
    
    # 좌석에 학생들 배치
    def arrage_students():
        for student_number, student_prefer in students_infos.items():
            _, _, r, c = choose(student_number, student_prefer)[0]
            board[r][c] = student_number
            # print(f"배치학생: {student_number}")
            # for row in board:
            #     print(row)
            # print("=" * 20)
    
    def cal_satis():
        sum_val = 0
        for r in range(n):
            for c in range(n):
                cnt = 0
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if in_range(nr, nc) and\
                        board[nr][nc] in students_infos[board[r][c]]:
                            cnt += 1
                if cnt == 0:
                    sum_val += 0
                elif cnt == 1:
                    sum_val += 1
                elif cnt == 2:
                    sum_val += 10
                elif cnt == 3:
                    sum_val += 100
                elif cnt == 4:
                    sum_val += 1000
                    
        return sum_val
    
    arrage_students()
    
    return cal_satis()
    
    
print(solution(n, students))