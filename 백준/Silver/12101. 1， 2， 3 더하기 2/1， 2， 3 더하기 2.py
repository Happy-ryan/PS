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

if n == 1:
    cnt = 1
    res = [1]
elif n == 2:
    cnt = 2
    res = [(1, 1), 2]
elif n == 3:
    cnt = 4
    res = [(1, 1, 1), (1, 2), (2, 1), 3]
else:
    for length in range(2, n + 1):
        dfs(0, length, n)

# print(res)
# print(cnt)

if k - 1 >= cnt:
    print(-1)
else:
    if type(res[k-1]) is int:
        print(res[k-1])
    else:
        print('+'.join(list(map(str, res[k-1]))))