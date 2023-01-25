def solution(cards):
    global cnt
    answer = []
    cards = [0] + cards
    adj = [[] for _ in range(len(cards))]
    
    for i, x in enumerate(cards):
        adj[i].append(x)

    visited = [False] * len(cards)
    
    def dfs(cur):
        global cnt
        visited[cur] = True
        cnt += 1
        for nxt in adj[cur]:
            if not visited[nxt]:
                dfs(nxt)

    for st in cards:
        if not visited[st] and st != 0:
            cnt = 0 
            dfs(st)
            answer.append(cnt)
            
    answer.sort( reverse= True )
    if len(answer) >= 2:
        return answer[0] * answer[1]
    else:
        return 0