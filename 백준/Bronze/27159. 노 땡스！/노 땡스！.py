# https://www.acmicpc.net/problem/27159


def split_(row):
    ans = []
    stack = []
    for x in row:
        if len(stack) == 0:
            stack.append(x)
        else:
            if x - stack[-1] == 1:
                stack.append(x)
            else:
                ans.append(stack)
                stack = []
                stack.append(x)
    ans.append(stack)
    return ans


n = int(input())
arr = list(map(int, input().split()))

ans = 0
for row in split_(arr):
    ans += min(row)
print(ans)
    