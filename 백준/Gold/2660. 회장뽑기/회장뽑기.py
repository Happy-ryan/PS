n = int(input())
# n <= 50
friends = []
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friends.append((a, b))

from collections import deque
from heapq import heappush, heappop


def solution(n, friends):
    inf = int(1e18)
    # 서로 친구이므로 양방향성!
    adj = [[] for _ in range(n + 1)]
    for friend in friends:
        a, b = friend
        adj[a].append(b)
        adj[b].append(a)
    # 그래프 문제는 확실..bfs, dfs 상관 없을 것 같음.
    # 특정한 회원 기준 가장 멀리 떨어진 친구가 얼마인가가 이 회원의 번호를 결정함!

    # sol1. bfs
    def bfs(start):

        visited = [False for _ in range(n + 1)]
        dist = [-inf for _ in range(n + 1)]

        dq = deque([])
        dq.append(start)
        visited[start] = True
        dist[start] = 0

        while dq:
            cx = dq.popleft()

            for nx in adj[cx]:
                if not visited[nx]:
                    dq.append(nx)
                    visited[nx] = True
                    dist[nx] = dist[cx] + 1

        return max(dist)

    # 시간복잡도 O(N + E) * N
    min_score = inf
    candidates = []
    for num in range(1, n + 1):
        # print(f"num: {num}, dist: {bfs(num)}")
        k = bfs(num)
        min_score = min(min_score, k)
        heappush(candidates, (k, num))

    # print(candidates)
    answer = []
    while True:
        person = heappop(candidates)
        if person[0] != min_score:
            break
        if not candidates:
            answer.append(person[1])
            break
        answer.append(person[1])
        
    print(min_score, len(answer))
    print(*answer)

solution(n, friends)