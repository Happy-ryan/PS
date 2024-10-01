# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

from collections import Counter
def solution(n, m, b, board):
    inf = int(1e18)
    ans_time = inf
    ans_high = -inf
    # 작업1. 맨 위의 블록을 제거하여 인벤토리에 넣을 수 있음. (2초)
    # 작업2. 인벤토리의 블록 하나를 맨 위의 블록에 놓을 수 있음. (1초)
    
    # 목적: 땅 고르기 작업에 걸리는 시간을 최소화하고 그 때의 땅의 높이를 구하라
    # 1 2  3  4
    # 5 6  7  8
    # 9 10 11 12
    # 땅의 높이가 높은 것이 또 좋움...
    # 따라서 특정 높이를 타겟으로 만들었을 때 시간을 확인하고 시간 -> 높이 우선순위가 존재한다!
    dic = Counter()
    for r in range(len(board)):
        for c in range(len(board[0])):
            dic[board[r][c]] += 1
    
    # 특정 높이가 되도록 만들 때 걸리는 시간 파악하는 함수
    def target_high(target_h, b):
        nonlocal ans_time, ans_high
        time = 0
        inventory = [0, 0] # (제거해서 인벤토리에 추가, 블록쌓아서 인벤토리에서 제거)
        # 시간복잡도(N*M)
        for height, value in dic.items():
            if height == target_h:
                continue
            minus_high = abs(height- target_h)
            # 블록 제거 > 인벤토리에 추가
            if height > target_h:
                inventory[0] += minus_high * value
            # 블록 추가 > 인벤토리에 제거
            elif height < target_h:
                inventory[1] += minus_high * value
        if inventory[0] + b >= inventory[1]:
            time += 2 * inventory[0]
            time += inventory[1]
            if (ans_time > time) or (ans_time == time and ans_high < target_h):
                ans_time = time
                ans_high = target_h
    ans = []
    # 시간복잡도(HIGH*HIGH)
    for high in range(0, 257):
        ans.append(target_high(high, b))
    
    return ans_time, ans_high

print(*solution(n, m, b, board))