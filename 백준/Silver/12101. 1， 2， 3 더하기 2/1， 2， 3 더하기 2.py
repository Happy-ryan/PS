import sys
sys.setrecursionlimit(10**5)

n, k = map(int, input().split())
arr = [1, 2, 3]
visited = []
res = []
cnt = 0

def dfs(lev, length, target):
    global cnt
    if lev == length:  
        if sum(visited) == target: 
            # print(visited)
            case = tuple(visited.copy())
            res.append(case)
            res.sort()
            cnt += 1
            return
        else: # 합이 되지 않을 때는 함수 종료시켜야함
            return

    for i in range(len(arr)):
        visited.append(arr[i])
        dfs(lev + 1, length, target)
        visited.pop()



for length in range(1, n + 1):
    dfs(0, length, n)

if k - 1 >= cnt:
    print(-1)
else:
    print('+'.join(list(map(str, res[k-1]))))
