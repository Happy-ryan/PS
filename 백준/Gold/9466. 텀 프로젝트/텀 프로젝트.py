import sys
sys.setrecursionlimit(10**5)

t = int(input())

def solution(n, students):
    global cycle_people, cycle_cnt
    # 모든 팀원이 서로 서로 지목하여 하나의 사이클이 만들어져야함!!
    # 4 -> 7 -> 6 -> 4 : 하나의 사이클 발생!!
    # 3 -> 3 : 자기 자신을 선택하는 것도 하나의 사이클이 된다!
    
    # 단순 방문으로만 체크하면 사이클 판단 불가능
    # 방문을 좀 더 자세하게 나눌 필요가 있어보임!
    # 유형1. 탐색시작 
    # 유형2. 탐색중
    # 유형3. 탐색완료
    # 4(방문) -> 7 -> 6 -> 4(재방문)
    
    # out degree 1인 그래프..!! > 모든 사이클을 찾을 수는 없지만 사이클의 유무 판단
    
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i].append(students[i - 1])
    
    # 탐색시작(0) / 탐색중(1) / 탐색완료(2)
    visited = [0 for _ in range(n + 1)]
    step= []
    cycle_people = 0
    cycle_cnt = 0
    def dfs(num):
        global cycle_people, cycle_cnt
        # 탐색 중
        visited[num] = 1
        # step 기록 - 백트래킹처럼
        step.append(num)
        for x in adj[num]:
            if visited[x] == 0:
                dfs(x)
            # 탐색중 + 탐색중 = 사이클 발견!!!! 원래는 사이클 발견만 하는 함수!
            elif visited[x] == 1:
                cycle_cnt += 1 
                idx = step.index(x)
                # 사이클에 포함된 사람의 수([4(*), 7, 6])
                cycle_people += len(step) - idx 
        # 탐색 완료
        visited[num] = 2
        # step 기록 - 백트래킹처럼
        step.pop()
    
    for num in range(1, n + 1):
        # 탐색시작
        if visited[num] == 0:
            dfs(num)
            
    return n - cycle_people
        
for _ in range(t):
    n = int(input())
    students = list(map(int, input().split()))
    print(solution(n, students))