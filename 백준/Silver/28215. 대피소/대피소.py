n, k = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(n)]

from itertools import combinations

def solution(n, k, houses):
    
    inf = int(1e18)
    
    def cal_dis(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # 시간복잡도 nCk 
    # ans = []
    ans = inf
    for row in combinations(range(n), k): # N개의 집 ~ K개의 보호소 선택
        # -inf > 내가 보호소일 경우 거리가 0
        dist_1 = 0
        for house in range(n): 
            if house not in set(row): # 보호소로 선택되지 않은 집에서 보호소까지의 거리 체크
                dist = inf
                for x in row:
                    dist = min(dist, cal_dis(houses[house], houses[x]))
                dist_1 = max(dist_1, dist)
        ans = min(ans, dist_1)
    
    return ans
    
print(solution(n, k, houses))