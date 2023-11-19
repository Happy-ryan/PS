# https://www.acmicpc.net/problem/13335
from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))

q = deque([])
t = 0
while trucks:
    truck = trucks[0]
    # q의 길이가 w와 같다는 것은 현재 가장 왼쪽의 트럭이 다음 트럭이 들어오면 다리를 벗어난다는 의미이다.
    if len(q) == w:
        q.popleft()
    if sum(q) + truck <= L:
        truck = trucks.popleft()
        q.append(truck)
    # 트럭을 이동시키기 위한 방법: 무게에는 영향을 안주면서 이동을 시키기 -> 0 넣기
    else:
        q.append(0)
    t += 1
# 마지막 트럭이 q에 진입하면 trucks는 0이 된다.
# 그러므로 t에 마지막 트럭의 이동시간을 더해줘야 모든 트럭들이 다리를 건너는 시간이 된다.
print(t + w)