n = int(input())
nodes = list(map(int, input().split()))
del_node = int(input())

def solution(n, nodes, del_node):
    
    adj = [[] for _ in range(n)]
    # print(adj)
    # print(nodes)
    for idx, node in enumerate(nodes):
        if node != -1:
            adj[node].append(idx)
            
    # 리프노드 = ajd에서 []인 것들! > 자식이 없기 때문!
    leaf_node = []
    for idx, row in enumerate(adj):
        if not len(row):
            leaf_node.append(idx)

    # print(leaf_node)
    
    visitd = [False] * (n)
    def dfs(node):
        if visitd[node]:
            return
        visitd[node] = True
        
        for x in adj[node]:
            dfs(x)
    
    
    dfs(del_node)
    
    # print(visitd)
    
    # 방문한 노드 제외
    cnt = len(leaf_node)
    for leaf in leaf_node:
        if visitd[leaf]:
            cnt -= 1
            
    # 틀린 이유 : -1 노드가 두 개의 자식 노드가 있으면 부모 노드는 절대 자식노드 될 수 없음
    # 문제는, 트리가 한 줄로 되어있을 때 자식이 죽어도 리프노드는 계속 새로 생성됨!
    
    if del_node == nodes.index(-1):
        return 0
    
    par = nodes[del_node] # 지운 node의 부모
    par_size = len(adj[par]) # 부모 node 자식의 수
    if par_size == 1:
        cnt += 1
    
    return cnt
        
print(solution(n, nodes, del_node))