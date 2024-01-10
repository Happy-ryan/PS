# https://www.acmicpc.net/problem/6198
n = int(input())
highs = [int(input()) for _ in range(n)]

stack = []
total_val = 0

for idx, high in enumerate(highs):
    while stack:
        if stack[-1][1] <= high:
            stack.pop()
        else:
            total_val += len(stack)
            break
        
        
    stack.append((idx, high))

# stack에 내림차순으로 쌓기...(monoton - 단조성)
# 나(high) 들어왔을 때 나보다 큰 놈은 stack에 존재함
# 따라서 나를 볼 수 있는 큰 놈들의 수를 더하면 됨.
print(total_val)