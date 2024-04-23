# 슬라임 합성 비용을 최소로 하도록 하자!
# 4 5 6 이라는 슬라임이 존재한다.
# 앞에서부터 차례대로 합성한다고 했을 경우 전수조사하기 위해서는 n!을 해야한다. > 시간초과
# 따라서 전수조사는 아니다.

# 6 5 4 > 30 4 > 120
# 4 5 6 > 20 6 > 120
# 비용이 최소로 들기 위해서는 크기가 작은 슬라임부터 합성을 해야한다.

# 2 3 8 10 14
#   6 8 10 14 +6
#    48 10 14 +48
#    48 140 +140
#    48*140 +48*140

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def solution(slimes):
    # 정렬해도 무관함.
    slimes.sort()
    cost = 1
    mod = 1000000007

    if len(slimes) == 1:
        return 1

    heap = []
    for slime in slimes:
        heappush(heap, slime)

    while len(heap) != 1:
        slime_1 = heappop(heap) 
        slime_2 = heappop(heap) 
        new_slime = slime_1 * slime_2
        heappush(heap, new_slime)
        cost *= new_slime
        cost %= mod
        # print(f"new_slime: {new_slime}, heap: {heap}, cost: {cost}")

    return cost 


t = int(input())
for _ in range(t):
    n = int(input())
    slimes = list(map(int, input().split()))
    print(solution(slimes))