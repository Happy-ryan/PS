from collections import deque

def bfs(n, adj):
    cnts = []
    in_queue = [False] * (n + 1)

    q = deque([])

    for start in range(1, n + 1):
        if in_queue[start]:
            continue
        q.append(start)
        in_queue[start] = True
        cnt = 0
        while q:
            cur = q.popleft()
            cnt += 1
            for nxt in adj[cur]:
                if not in_queue[nxt]:
                    q.append(nxt)
                    in_queue[nxt] = True
        cnts.append(cnt)
    
    return cnts
    
def solution(n, wires):
    answer = int(1e18)
    for i in range(n - 1):
        adj = [[] for _ in range(n + 1)]
        for j, wire in enumerate(wires):
            if j == i:
                continue
            adj[wire[0]].append(wire[1])
            adj[wire[1]].append(wire[0])
        
        x, y = bfs(n, adj)
        answer = min(answer, abs(x - y))
        
    return answer