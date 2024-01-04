# https://www.acmicpc.net/problem/15666

n, m = map(int, input().split())
arr = list(set(map(int,input().split())))
arr.sort()
ans = []
last = []

def dfs(level):
    global last
    if level == m:
        if last != ans and sorted(ans) == ans:
            print(*ans)
        # last가 ans의 주소를 참조
        # last랑 ans가 동시에 참조됨.
        last = ans.copy()
        return
    for x in arr:
        ans.append(x)
        dfs(level+1)
        ans.pop()

dfs(0)