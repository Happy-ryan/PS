# n명의 손님, m개의 초밥을 순서대로 만듦
# 1번 초밥을 1번 인간이 먹었으면 2번 초밥도 1번 인간이 먹음
# 전제, 1번 인간의 주문 목록표에 1번, 2번 초밥 있는 경우
# 같은 종류의 초밥은 최대 1번만 먹음
# 주문목록과 초밥 만들어지는 순서가 주어질 때, 각 손님이 먹게 되는 초밥의 개수

from collections import deque

n, m = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(n)]
sushi_order = deque(list(map(int, input().split())))

# 초밥 m개가 만들어지고 만들어지고 나올 때 선입선출 <- 큐 O(1) * M번 = M = 200,000
# n개의 사람을 돌면서 <- O(N = 100,000)
# 결국 시간초과 발생

# 1. 절대 줄일수앖는걸 찾는다 > 초밥은 반드시 확인이 되어야하므로 초밥(O(M))은 절대적이다
# 2. 줄여야하는 문제를 명확히한다
# 3. 분리할 수 있는건 분리한다
def solution(n, m, orders, sushi_order):
    # 초밥의 순서는 고정이다 > 각 초밥을 먹을 사람들을 넣어놓자!
    # 초밥의 순서 돌 때 어떤 초밥에 어떤 사람이 예약되어있는지 큐로 넣어놓음
    sushi_court = [deque() for _ in range(max(sushi_order) + 1)]
    check = set(sushi_order)
    for idx, order in enumerate(orders):
        for sushi in order[1:]:
            if sushi not in check:
                continue
            sushi_court[sushi].append(idx)
            
    answer = [0] * n
    for sushi in sushi_order:
        if sushi_court[sushi]:
            answer[sushi_court[sushi].popleft()] += 1
            
    return answer

print(*solution(n, m, orders, sushi_order))