# https://www.acmicpc.net/problem/15686
# 시간복잡도: M<= 치킨집의 개수 <= 13
# 1) 치킨집 M개 선택: combination(치킨집, M)
# 2) 치킨집과 집까지의 치킨거리 계산: 한 치킨집 당 최대 2N번의 계산이 필요함
# 3) 치킨집과 집의 좌표 찾기: N^2
# -> 2*N*combinations(치킨집의 수, M) + N^2
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for row in range(n)]

def check(board):
    k = len(board)
    homes = []
    chickens = []
    for r in range(k):
        for c in range(k):
            if board[r][c] == 1:
                homes.append((r, c))
            elif board[r][c] == 2:
                chickens.append((r, c))
            else:
                continue
    return homes, chickens

def distance(homes, chickens):
    '''
    homes -> 집의 좌표모음 [( , )..]
    chickens -> 치킨집의 좌표모음 [( , )..]
    '''
    final_dis = 0
    for h_r, h_c in homes:
        dis = int(1e8)
        for ch_r, ch_c in chickens:
            dis = min(dis, abs(h_r - ch_r) + abs(h_c - ch_c))
        final_dis += dis
    return final_dis


def solution(m, board):
    homes = check(board)[0]
    chickens = check(board)[1]
    distance_candiate = int(1e8)
    for selected_chickens in combinations(chickens, m):
        distance_candiate = min(distance_candiate, distance(homes, selected_chickens))

    return distance_candiate

print(solution(m, board))
