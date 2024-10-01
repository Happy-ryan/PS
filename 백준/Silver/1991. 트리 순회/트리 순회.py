n = int(input())
nodes = [list(input().split()) for _ in range(n)]

from collections import defaultdict

def solution(n, nodes):
    
    graph = defaultdict(list)
    
    for node in nodes:
        graph[node[0]] = [node[1], node[2]]
        
    preorder_list = []
    def preorder(node):
        # 현재 노드
        preorder_list.append(node)
        # 왼쪽 자식
        if graph[node][0] != '.':
            preorder(graph[node][0])
        # 오른쪽 지식
        if graph[node][1] != '.':
            preorder(graph[node][1])
            
    preorder('A')
    print(''.join(preorder_list))
    
    inorder_list = []
    def inorder(node):
        # 왼쪽 자식
        if graph[node][0] != '.':
            inorder(graph[node][0])
        # 현재 노드
        inorder_list.append(node)
        # 오른쪽 자식
        if graph[node][1] != '.':
            inorder(graph[node][1])
    inorder('A')
    print(''.join(inorder_list))
    
    post_list = []
    def postorder(node):
        # 왼쪽지식
        if graph[node][0] != '.':
            postorder(graph[node][0])
        # 오른쪽 자식
        if graph[node][1] != '.':
            postorder(graph[node][1])
        # 현재 노드
        post_list.append(node)
            
    postorder('A')
    print(''.join(post_list))
    
solution(n, nodes)