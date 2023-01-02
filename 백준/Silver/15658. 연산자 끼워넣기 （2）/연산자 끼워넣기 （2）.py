n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
visited = [num[0]]
max_ans = -int(1e18)
min_ans = int(1e18)
def dfs(lev, num):
    global plus, minus, mul, div, max_ans, min_ans

    if lev == n:
        # if plus + minus + mul + div == n - 1: 횟수제한없음, 연산횟수 생각없이 lev까지 전부 계산
            x = visited[-1]
            max_ans = max(max_ans, x)
            min_ans = min(min_ans, x)
            return
        # else: 
        #     return

    if plus > 0:
        visited.append(visited[-1] + num[lev])
        plus -= 1
        dfs(lev + 1, num)
        plus += 1
        visited.pop()
    
    if minus > 0: 
        visited.append(visited[-1] - num[lev])
        minus -= 1
        dfs(lev + 1, num)
        visited.pop()
        minus += 1

    if mul > 0:
        visited.append(visited[-1] * num[lev])
        mul -= 1
        dfs(lev + 1, num)
        visited.pop()
        mul += 1

    if div > 0:
        if visited[-1] < 0:
            visited.append(-(-visited[-1] // num[lev]))
        else:
            visited.append(visited[-1] // num[lev])
        div -= 1
        dfs(lev + 1, num)
        visited.pop()
        div += 1

dfs(1, num)

print(max_ans)
print(min_ans)