# https://www.acmicpc.net/problem/2174
C, R = map(int, input().split())
N, M = map(int, input().split())

board = [[0 for _ in range(C)] for _ in range(R)]

# cur_dir 결정
def direction(prompt):
    if prompt == "E":
        return 0
    elif prompt == "S":
        return 1
    elif prompt == "W":
        return 2
    else:
        return 3
# 좌표계 좌표 변환(열좌표, 행좌표. 행의 수)
def convert_coordinates(c, r, R):
    new_r = R - 1 - r
    new_c = c
    return new_c, new_r
# 열, 행, 방향
robots =[['열', '행', '방향']] + [list(input().split()) for _  in range(N)]
for idx, robot in enumerate(robots):
    if idx != 0:
        # 인덱스1이 
        cc, cr = convert_coordinates(int(robot[0]) - 1,int(robot[1]) - 1, R)
        robots[idx] = [cc, cr, direction(robot[2])]
        board[cr][cc] = idx
# print(robots)
# 로봇번호 1base, 명령어, 반복회수
cmds = [list(input().split()) for _ in range(M)]

nr, nc = 0, 0
wall_flag = True
robot_flag = True

# 동남서북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 격자 내 이동
def in_range(r, c):
    return 0 <= r < R and 0 <= c < C
# `2개 이상일 때 로봇의 마지막 도착지를 결정할 수 있어야함.`
def simulate(robot_num, prompt, cnt, cr, cc, cur_dir):
    global nr, nc, wall_flag, robot_flag
    for _ in range(cnt):
        if prompt == "R":
            cur_dir = (cur_dir + 1) % 4
        elif prompt == "L":
            cur_dir = (cur_dir + 3) % 4
        else:
            nr = cr + dr[cur_dir]
            nc = cc + dc[cur_dir]
            if not in_range(nr, nc):
                wall_flag = False
                return robot_num, cur_dir, cr, cc
            else:
                if board[nr][nc] != 0:
                    robot_flag = False
                    return robot_num, cur_dir, nr, nc
            board[cr][cc] = 0
            cr, cc = nr, nc
            board[cr][cc] = robot_num
            # print("------------------판------------------")
            # for row in board:
            #     print(*row)
            # print("------------------판------------------")
    return robot_num, cur_dir, cr, cc
            
            
# print("가장 처음 로봇들의 상태", robots)
# print("-----" * 5)
for cmd in cmds:
    # 로봇번호(int), 명렁어(string), 반복회수(int)
    robot_num, prompt, cnt = int(cmd[0]), cmd[1], int(cmd[2])
    # 로봇의 위치 : 열(int), 행(int), 방향(int)
    cc, cr, cur_dir = robots[robot_num][0], robots[robot_num][1], robots[robot_num][2]
    # print("로봇의 번호",robot_num, "현재 위치", "행:", cr, "열", cc, "방향:", cur_dir,"회수:", cnt)
    robot_num, cur_dir, nr, nc = simulate(robot_num, prompt, cnt, cr, cc, cur_dir)
    # print("----" * 5)
    # print(f"{robot_num}로봇이 이동했습니다.", "이동 후 좌표", "행:",nr,"열:", nc, "방향:", cur_dir)
    # print("------------------판------------------")
    # for row in board:
    #     print(*row)
    # print("------------------판------------------")
    if not robot_flag:
        print(f"Robot {robot_num} crashes into robot {board[nr][nc]}")
        break
    if not wall_flag:
        print(f"Robot {robot_num} crashes into the wall")
        break
    robots[robot_num] = [nc, nr, cur_dir]
    # print("----" * 5)
    # print(f"로봇{robot_num} 좌표 변경 후", robots)
    # print(f"\n----로봇{robot_num}의 이동 종료---\n")
    
if wall_flag and robot_flag:
    print("OK")