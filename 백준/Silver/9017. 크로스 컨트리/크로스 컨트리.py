def solution(n, order):
    # 각 팀의 참가 선수가 여섯보다 작으면 계산에서 제외
    # 6명 사람 중 상위 네 명의 주자의 점수 합 > 가장 낮은 점수 얻은 팀이 우승
    # 동점의 경우, 다섯 번째 주자 먼저 들어온 사람 우승
    
    from collections import Counter, defaultdict
    
    def cal():
        team = Counter()
        for o in order:
            team[o] += 1
        ans = defaultdict(list)
        for k, v in team.items():
            if v == 6:
                ans[k] = []
        return ans
    
    team = cal()
    sc = cal()
    score = 1
    
    for idx, o in enumerate(order):
        if o in team:
            team[o].append(idx)
            sc[o].append(score)
            score += 1
    
    for k in team.keys():
        team[k].sort()
        sc[k].sort()
    
    ans = []
    max_score = 0
    for k in team.keys():
        # 점수
        score = sum(sc[k][0:4])
        max_score = max(max_score, score)
        # 5번째 도착
        idx = team[k][4]
        ans.append((score, idx, k))
    
    # 점수 합계 낮은 순 > 5번째 도착 순
    ans.sort(key=lambda x : (x[0], x[1]))
    

    return ans[0][2]
        
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    order = list(map(int, input().split()))
    print(solution(n, order))