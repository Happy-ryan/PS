n = int(input())
num = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
visited = [num[0]]
max_ans = -int(1e18)
min_ans = int(1e18)
def dfs(lev, num):
    global plus, minus, mul, div, max_ans, min_ans
    
    if lev == n:
        if plus == 0 and minus == 0 and mul == 0 and div == 0:
            x = visited[-1]
            max_ans = max(max_ans, x)
            min_ans = min(min_ans, x)
            return
        else: 
            return
    visited.append(visited[-1] + num[lev])
    plus -= 1
    dfs(lev + 1, num)
    plus += 1
    visited.pop()

    visited.append(visited[-1] - num[lev])
    minus -= 1
    dfs(lev + 1, num)
    visited.pop()
    minus += 1

    visited.append(visited[-1] * num[lev])
    mul -= 1
    dfs(lev + 1, num)
    visited.pop()
    mul += 1

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