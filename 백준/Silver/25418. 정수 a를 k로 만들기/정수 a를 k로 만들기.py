from collections import deque

a, k = map(int, input().split())
in_queue = {}
visited = {}

def bfs(a, k):
    dq = deque([])
    
    dq.append(k)
    in_queue[k] = True
    visited[k] = 0
    
    while dq:
        cur = dq.popleft()
        num_list = [cur - 1]
        if cur % 2 == 0:
            num_list.append(cur // 2)
        if a not in num_list:
            for nxt in num_list:
                if nxt not in in_queue:
                    dq.append(nxt)
                    in_queue[nxt] = True
                    visited[nxt] = visited[cur] + 1
        else:
            visited[a] = visited[cur] + 1
            break
                
    return visited[a]

print(bfs(a, k))