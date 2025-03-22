n, k = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

from heapq import heappush, heappop

def solution(n, k, infos):
    # 1. 3월 - 같은 포지션 중 선수 가치가 가장 높은 선수 선발 - 여러명 / 아무나
    #   1-1. 해당 포지션에 선수 없을 지 공석
    # 2. 8월 - 현재 팀에 선발된 선수의 가치 -1 하락. 0 최저
    # 3. 11월에 1의 조건대로 선발 선수 재구성.
    
    inf = int(1e18)
    
    team = [-inf] * 12
    
    # 선수 넣기 - max 힙
    pos = [[] for _ in range(12)]
    for p, w in infos:
        heappush(pos[p], -w)
        
    def one_year():
        # 3월 - 선발
        for p in range(12):
            # 해당 포지션의 후보 선수 초기화
            candidate = 0
            # 해당 포지션의 후보 선정
            if pos[p]:
                candidate = -heappop(pos[p])
            
            # 선발선수가 없다면 - 후보선수 => 선발선수
            if team[p] == -inf:
                team[p] = candidate
            # 선발선수가 있다면 - 후보선수 vs 선발선수 비교
            else:
                # 선발선수와 후보선수 가치 비교하기
                    # 선발선수가 크면 후보선수는 다시 들어감
                if team[p] >= candidate:
                    heappush(pos[p], -candidate)
                    # 후보선수가 크면 선발선수가 들어감
                else:
                    heappush(pos[p], -team[p])
                    team[p] = candidate
                
        # print(f"3월 선발팀 구성 및 가치 : {team}")
        # print(f"3월 후보팀 구성 및 가치 : {pos}")
        
        # 8월 - 가치하락
            # 선발 선수 전체적으로 -1
        for p in range(12):
                team[p] -= 1
                team[p] = max(team[p], 0)
        # print(f"8월 선발팀 구성 및 가치 : {team}")
        # print(f"8월 후보팀 구성 및 가치 : {pos}")
        
        # 11월 - 재구성
        for p in range(12):
            # 해당 포지션의 후보 선수 가치 초기화
            candidate = 0
            # 해당 포지션의 후보 선정
            if pos[p]:
                candidate = -heappop(pos[p])

            # 선발선수와 후보선수 가치 비교하기
                # 선발선수가 크면 후보선수는 다시 들어감
            if team[p] >= candidate:
                heappush(pos[p], -candidate)
                # 후보선수가 크면 선발선수가 들어감
            else:
                heappush(pos[p], -team[p])
                team[p] = candidate        
        # print(f"11월 선발팀 구성 및 가치 : {team}")
        # print(f"11월 후보팀 구성 및 가치 : {pos}")
        
        return sum(team)

    for y in range(k):
        # print(f"======={y + 1}년=======")
        team_value = one_year()
    
    return team_value
        
print(solution(n, k, infos))