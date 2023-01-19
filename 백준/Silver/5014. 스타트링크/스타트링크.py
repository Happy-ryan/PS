from collections import deque
def solution(F, S, G, U, D):   
    inf = int(1e18) 
    in_queue = [False] * (1 + F)
    dist = [inf] * (1 + F)

    dx = [U, -D]

    def check(x):
        return 0 < x < F + 1 and not in_queue[x]

    q = deque([])
    q.append(S)
    in_queue[S] = True
    dist[S] = 0

    while q:
        cur = q.popleft()
        for k in range(2):
            nxt = cur + dx[k]
            if check(nxt):
                q.append(nxt)
                in_queue[nxt] = True
                dist[nxt] = dist[cur] + 1

    if dist[G] >= inf:
        return "use the stairs"
    else:
        return dist[G]


F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))