# https://www.acmicpc.net/problem/26583

def cal(row):
    ans = [0] * len(row)
    for i, x in enumerate(row):
        if i == 0:
            ans[i] = row[0] * row[1]
        elif i == len(row) - 1:
            ans[i] = row[-1] * row[-2]
        else:
            ans[i] = row[i - 1] * row[i + 1] * row[i]
    return ans

# import sys
# input = sys.stdin.readline

while True:
    try:
        row = list(map(int, input().split()))
        print(*cal(row))
    except EOFError:
        break
        