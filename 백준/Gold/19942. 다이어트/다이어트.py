n = int(input())
must_portion = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

inf = int(1e18)
def check(step):
    sum_val = [0, 0, 0, 0, 0]
    for i in step:
        for k in range(5):
            sum_val[k] += board[i][k]
    
    for k in range(4):
        if sum_val[k] < must_portion[k]:
            return -1
    return sum_val[4]

def solution(n, must_portion, board):
    min_ans = []
    step = []
    def dfs(idx):
        nonlocal min_ans
        if idx == n:
            res = check(step)
            if res != -1:
                min_ans.append((res, step.copy()))
            return
        
        # 선택함
        step.append(idx)
        dfs(idx + 1)
        step.pop()
        
        # 선택안함
        dfs(idx + 1)
        
    dfs(0)
    min_ans.sort(key=lambda x: (x[0], x[1]))
    
    if len(min_ans) == 0:
        return -1
    
    res1 = min_ans[0][0]
    step = min_ans[0][1]
    for i in range(len(step)):
        step[i] += 1
        step[i] = str(step[i])
    step = ' '.join(step)
    return f"{res1}\n{step}"

print(solution(n, must_portion, board))