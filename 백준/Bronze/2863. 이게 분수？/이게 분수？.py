board = [list(map(int, input().split())) for _ in range(2)]

def simulate():
    tmp = board[0][1]
    board[0][1] = board[0][0]
    board[0][0] = board[1][0]
    board[1][0] = board[1][1]
    board[1][1] = tmp

def cal():
    return (board[0][0] / board[1][0]) + (board[0][1] / board[1][1])

ans = []
max_ans = cal()
ans.append((0, max_ans))
for i in range(1, 4):
    simulate()
    ans.append((i, cal()))

ans.sort(key= lambda x: (-x[1], x[0]))

print(ans[0][0])