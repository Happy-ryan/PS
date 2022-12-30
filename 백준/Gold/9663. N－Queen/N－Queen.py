import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

up = [0] * N
left = [0] * (2*N)
right = [0] * (2*N)

def check(r,c):
    if up[c] == 1 or left[r - c] == 1 or right[r + c] == 1:
        return False
    return True

def dfs(lev):
    global cnt
    if lev == N:
        cnt += 1

    for col in range(N):
        if check(lev, col):
            up[col] = 1
            left[lev - col] = 1
            right[lev + col] = 1
            dfs(lev + 1)
            up[col] = 0
            left[lev - col] = 0
            right[lev + col] = 0

dfs(0)

print(cnt)
