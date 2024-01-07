# https://www.acmicpc.net/problem/16922

n = int(input())

numbers = [1, 5, 10, 50]
cnt = set()
ans = []
def dfs(level, idx):
    if level == n:
        sum_val = sum(ans.copy())
        cnt.add(sum_val)
        return
    # 나보다 큰 인덱스만 바라보도록 하기
    # idx - 0: 0 1 2 3 
    # idx - 1: 1 2 3 
    for i in range(idx, 4):
        ans.append(numbers[i])
        dfs(level + 1, i)
        ans.pop()
        
dfs(0, 0)
print(len(cnt))