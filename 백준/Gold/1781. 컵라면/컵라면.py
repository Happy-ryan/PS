N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]

from heapq import heappop, heappush

def solution(N, infos):
    
    # 관점1. 데드라인 짧은 순대로 풀기
    # 관점2. 컵라면 많은 순서대로 풀기
    # 관점3. 데드라인은 짧고 컵라면은 많은 순서
    # 관점4. 데드라인이 길고 컵라면은 많은 순서
    heap1 = []
    heap2 = []
    heap3 = []
    heap4 = []
    heap5 = []
    heap6 = []
    heap7 = []
    heap8 = []
    for info in infos:
        deadline, cup = info

        # heappush(heap1, (cup, deadline))
        # heappush(heap2, (deadline, cup))
        
        # heappush(heap3, (-cup, deadline))
        heappush(heap4, (deadline, -cup)) # 데드라인은 짧고 컵라면은 많은 수
        
        # heappush(heap5, (cup, -deadline))
        # heappush(heap6, (-deadline, cup))
        
        # heappush(heap7, (-cup, -deadline))
        # heappush(heap8, (-deadline, -cup))
    
    
    def act(heap, idx):
        cnt = 0
        while heap:
            deadline, cup = heappop(heap)
            if idx % 2 != 0:
                cup, deadline = deadline, cup
            
            if deadline < 0:
                deadline = -deadline
            if cup < 0:
                cup = -cup
                
            # # deadline이 선택된 컵라면 수(문제 푼 회수 = 시간)보다 크면 먹으면 된다.
            # # 뒤에 더 좋은 케이스가 나오면 아까 먹은 컵라면 중에서 최소로 먹은 것은 제외하는게 좋음.
            # 먹기 전에 판단을 함.
            if deadline > len(selected):
                heappush(selected, cup)
            else:
                # 확인하자...
                min_cup = selected[0]
                if min_cup < cup:
                    heappop(selected)
                    heappush(selected, cup)
                
            #     # cnt += cup
            #     print(f"selected: {selected}, deadline: {deadline}, cup: {cup}, cnt: {cnt}")
            #     # cur_time += 1
            # heappush(selected, cup)  # 일단 무조건 먹기
            
            # if len(selected) > deadline: # 내가 하나를 먹어서 데드라인보다 커지는 경우
            #                             # 그러므로 금방 먹은것까지해서 최소 컵라면을 지우면 최적
            #     heappop(selected)  # 최소값 토해내기
                
        return sum(selected)
    
    # cnt = 0
    # for idx, heap in enumerate([heap1, heap2, heap3, heap4, heap5, heap6, heap7, heap8]):
        # selected = []
        # val = act(heap, idx + 1)
    #     cnt = max(cnt, val)
    #     # print(f"heap: heap{idx + 1} cnt: {cnt}, val : {val}")
    #     # print('=')
    
    selected = []
    val = act(heap4, 4)
    
    return val

print(solution(N, infos))