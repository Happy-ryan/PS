# 조건1 : ICN공항에서 출발
# 조건2 : 모든 항공권을 사용해야함 & 중복x > used 사용
# 조건3 : 스페셜저지 > 알파벳 순서 앞서는 것
from functools import cmp_to_key
        
def solution(tickets):
    answer = []
    for i, ticket in enumerate(tickets):
        if ticket[0] == 'ICN': # 시작점 미리 설정 dfs(1, tickets) > 1부터 시작
            visited = [ticket[0], ticket[1]]
            used = [0] * len(tickets)
            used[i] = 1 # 티켓 모두 사용 > 중복 금지 > used 사용
            
            def dfs(lev, tickets):
                if lev == len(tickets): # 티켓의 갯수만큼 재귀
                    a = visited.copy()
                    answer.append(''.join(a))
                    return
                for i, new_ticket in enumerate(tickets):
                    if used[i] == 0:
                        if new_ticket[0] == visited[-1]: # 전 여행지의 도착점과 다음 여행지의 출발점이 동일
                            used[i] = 1
                            visited.append(new_ticket[1])
                            dfs(lev + 1, tickets)
                            visited.pop()
                            used[i] = 0
            dfs(1, tickets)
    answer.sort() # 도착지점 join으로 합친 후에 정렬
    
    final = []
    ans = answer[0]
    for i in range(0, len(ans), 3):
        final.append(ans[i : i + 3]) # 3개씩 출력
        
    return final