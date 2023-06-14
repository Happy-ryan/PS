# https://www.acmicpc.net/problem/9742
# 322 는 감소하는 수 아님 > 무조건 내림차순 해야함.
from functools import cmp_to_key

used = [0] * 10
visited = [10]

def compare(앞, 뒤):
    if 앞 == 뒤:
        return 0
    elif 앞 > 뒤:
        return 1
    else:
        return -1

def arr2num(arr: list) -> int:
    ans = 0
    for i in range(len(arr)):
        ans += arr[i] * (10 ** (len(arr) - i - 1))
    return ans


def dfs(level, depth):
    if level == depth:
        # print(*visited[1:])
        # print(arr2num(visited[1:]))
        return arr2num(visited[1:])
    num_list = ""
    for i in reversed(range(10)):
        if used[i] == 0 and visited[-1] > i:
            used[i] = 1
            visited.append(i)
            num_list += str(dfs(level + 1, depth)) + " "
            # num_list.append(num)
            used[i] = 0
            visited.pop()
    return num_list


ans = ""
for i in range(1, 11):
    ans += dfs(0, i)

ans = ans.split(" ")
ans_list = []
for x in ans:
    if x.isdigit():
        ans_list.append(int(x))

ans_list.sort(key=cmp_to_key(compare))
        
n = int(input())
if len(ans_list) <= n:
    print(-1)
else:
    print(ans_list[n])