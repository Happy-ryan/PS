# https://www.acmicpc.net/problem/23841


def change(row):
    n = len(row)
    ans = [str(0)] * n
    for i, x in enumerate(row):
        if x != ".":
            ans[i] = x
            ans[n - i - 1] = x
    ans = ''.join(ans)
    ans = ans.replace('0','.')
    return ans
    
    
r, c = map(int, input().split())

for _ in range(r):
    row = input()
    print(change(row))