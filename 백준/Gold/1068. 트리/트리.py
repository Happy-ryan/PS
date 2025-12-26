N = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())

def solution(N, nodes, del_node):
    global cnt
    cnt = 0
    adj = [[] for _ in range(N)]
    for idx, num in enumerate(nodes):
        if num == -1 or idx == del_node:
            continue
        adj[num].append(idx) # idx가 노드번호
        
    # 삭제노드 = 방문 물가 > visited 기록
    visited = [False for _ in range(N)]
    visited[del_node] = True
    
    leaf_nodes = []
    def dfs(cur, lv):
        global cnt
        # cnt = 0
        visited[cur] = True # 방문체크
        
        # 리프노드 체크
        if len(adj[cur]) == 0:
            cnt += 1
            leaf_nodes.append(cur)
        # print(f"방문 :{cur}, visited: {visited}, lv :{lv}, cnt: {cnt}")
        for nxt in adj[cur]:
            if not visited[nxt]:
                dfs(nxt, lv + 1)
                # cnt += 1
        # # cnt 똑같이 0이라는건 방문한게 없다는 것 > 리프노드
        # if cnt == 0: 
        #     leaf_nodes.append(cur)

    root = nodes.index(-1)
    
    # print(adj, root)
    if root == del_node:
        return 0
    
    dfs(root, 0)
    
    # print(leaf_nodes)
    
    # return len(leaf_nodes)
    return cnt
    
print(solution(N, nodes, del_node))