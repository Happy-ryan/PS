A,B,N,M = map(int,input().split())

in_queue = [False]*100001
dist = [0]*100001

move = [1,-1,+A,-A,+B,-B,A,B]

def check(x):
    return 0<= x <= 100000

from collections import deque
q = deque([N])

while q:
    cur = q.popleft()
    in_queue[cur] = True
    for k in range(8):
        if k == 6:
            nxt = cur*move[k]
        elif k == 7:
            nxt = cur*move[k]
        else:
            nxt = cur + move[k]

        if check(nxt) and\
            not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True
            dist[nxt] = dist[cur] + 1

print(dist[M])