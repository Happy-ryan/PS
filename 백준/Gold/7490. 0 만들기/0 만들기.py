# https://www.acmicpc.net/problem/7490
# 시간복잡도: 3^9  

def str_eq2num(ans:str) -> int: 
    ret = 0
    # --원본을 유지하자! 꼭 기억하기
    ans_concat = ans.replace(" ", "")
    ret = eval(ans_concat)
    if ret == 0:
        print(ans[1:])


def arr2eq(visited:list) -> str:
    num = list(range(1, len(visited) + 2))
    ans = "+"
    for idx in range(len(visited)):
        ans += str(num[idx])
        ans += visited[idx]
    ans += str(num[-1])
    return ans

# n은 숫자의 개수
visited = []
def dfs(level, n):
    if level == n - 1:
        str_eq2num(arr2eq(visited))
        return
    # -- ASCII 순서 > 공백, 더하기, 빼기
    for i in sorted([" ", "+", "-"]):
        visited.append(i)
        dfs(level + 1, n)
        visited.pop()

t = int(input())
for _ in range(t):
    n = int(input())
    dfs(0, n)
    print()