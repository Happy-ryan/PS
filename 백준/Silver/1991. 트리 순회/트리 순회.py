# https://www.acmicpc.net/problem/1991
from collections import defaultdict

n = int(input())
nodes = [list(input().split()) for _ in range(n)]
tree = defaultdict(list)
root_node = 'A'

for root, right, left in nodes:
    tree[root].append(right)
    tree[root].append(left)

def preorder(root: str):
    if tree[root][0] == '.' and tree[root][1] == '.':
        print(root, end="")
        return
    
    left = tree[root][0]
    right = tree[root][1]
    
    print(root, end="")
    
    if left != '.':
        preorder(left)
        
    if right != '.':
        preorder(right)


def inorder(root):
    if tree[root][0] == '.' and tree[root][1] == '.':
        print(root, end="")
        return
    
    left = tree[root][0]
    right = tree[root][1]
    
    if left != '.':
        inorder(left)
        
    print(root, end="")
    
    if right != '.':
        inorder(right)


def postorder(root):
    if tree[root][0] == '.' and tree[root][1] == '.':
        print(root, end="")
        return

    left = tree[root][0]
    right = tree[root][1]
    
    if left != '.':
        postorder(left)
        
    if right != '.':
        postorder(right)
        
    print(root, end="")
    

preorder(root_node)
print()
inorder(root_node)
print()
postorder(root_node)
