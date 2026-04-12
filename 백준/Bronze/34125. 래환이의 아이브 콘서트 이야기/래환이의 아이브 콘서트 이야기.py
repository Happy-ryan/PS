n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

arr = []

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i - 1][j - 1] == 1:
            continue
        d = i + abs((m + 1) // 2 - j)
        arr.append((d, i, j))
        
arr.sort(key=lambda x : x[0])

if not arr:
    print(-1)
else:
    print(arr[0][1], arr[0][2])