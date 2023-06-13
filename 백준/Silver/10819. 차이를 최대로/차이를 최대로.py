# https://www.acmicpc.net/problem/10819
# 시간복잡도: 8! > 40320 : n!

n = int(input())
arr = list(map(int, input().split()))

def sub(arr:list):
    ans = 0
    for i in range(len(arr) - 1):
        ans += abs(arr[i] - arr[i + 1])
    return ans

used = [0] * n
visited = []
# 출발점이 트리의 시작점들...
# 팩토리얼 만들기
def dfs(cur):
    if cur == n:
        # print(*visited)
        return sub(visited)
    # 각각의 인덱스만큼이 dfs 시작점의 수
    ret = 0
    for i in range(n):
        if used[i] == 0:
            used[i] = 1
            visited.append(arr[i])
            ret = max(ret, dfs(cur + 1))
            used[i] = 0
            visited.pop()
    return ret
print(dfs(0))
