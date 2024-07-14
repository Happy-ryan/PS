t = int(input())
cmds = [list(map(int, input().split())) for _ in range(t)]

score = 0
stack = []

for idx, cmd in enumerate(cmds):
    if cmd[0] == 0:
        if not stack:
            continue
        if stack:
            work = stack.pop()
            work[1] -= 1
        if work[1] == 0:
            score += work[0]
        else:
            stack.append(work)
    else:
        work = cmd[1:]
        work[1] -= 1
        if work[1] == 0:
            score += work[0]
        else:
            stack.append(work)
    # print(f"현재시각: {1 + idx}")
    # print(f"현재 스택 상황: {stack}")
    # print(f"현재 점수 상황: {score}")
    # print("=")

print(score)