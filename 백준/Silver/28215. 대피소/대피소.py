n, k = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(n)]

from itertools import combinations

def solution(n, k, houses):
    
    inf = int(1e18)
    
    def cal_dis(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    # 시간복잡도 nCk 
    ans = []
    for row in combinations(range(n), k): # N개의 집 ~ K개의 보호소 선택
        # print(f"선택한 보호소: {row}")
        dist_1 = []
        for house in range(n): 
            if house not in row: # 보호소로 선택되지 않은 집에서 보호소까지의 거리 체크
                dist = inf
                for x in row:
                    dist = min(dist, cal_dis(houses[house], houses[x]))
                    # dist_1.append(cal_dis(houses[house], houses[x]))
                    # print(f"집: {house}, 보호소까지의 거리: {cal_dis(houses[house], houses[x])}")
                # print(f"집: {house}, 집까지 보호소까자의 최댄거리:{dist} ")
                dist_1.append(dist)
                # print(dist_1)
            # dist_1 = min(dist_1, dist_2)
            # print(f"==== 집: {house} 끝 ====")
            # print(f"==== 선택한 보호소의 경우의 수 ==== ")
        ans.append(max(dist_1))
        # print(ans)
    # print(ans)
    
    return min(ans)
    
print(solution(n, k, houses))