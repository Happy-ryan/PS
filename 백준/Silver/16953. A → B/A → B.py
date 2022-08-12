A,B = map(int,input().split())

in_queue = {}
dist = {}

from collections import deque
q = deque([A])
in_queue[A] = True
dist[A] = 1
dist[B] = 0
while q:
    cur = q.popleft()
    num_list = [cur*2,cur*10+1]
    in_queue[num_list[0]] = True
    in_queue[num_list[1]] = True
    if B not in num_list:
        for nxt in num_list:
            if nxt <= B:
                q.append(nxt)
                dist[nxt] = dist[cur] + 1
            else:
                break
    else:
        dist[B] = dist[cur]+1
        break

if dist[B] == 0:
    print(-1)
else:
    print(dist[B])