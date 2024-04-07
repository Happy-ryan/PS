n = int(input())
cmds = [list(input()) for _ in range(n)]

from collections import deque


def solution(n, cmds):
    in_stack = deque([])

    for row in cmds:
        if row[0] != "3":
            in_stack.append((row[0], row[2]))
        # 가장 나중에 추가 된 블록!!
        # stack형태를 사용해 가장 나중에 추가된 블록 삭제
        # 왼쪽, 오른쪽에 넣을지 나중에 판단하기 위해서 cmd정보도 같이 stack에 쌓는다.
        else:
            # 비어있을 때는 pop할 수 없으니 예외처리
            if not in_stack:
                continue
            in_stack.pop()

    out_queue = deque([])

    for cmd, char in in_stack:
        if cmd == "1":
            out_queue.append(char)
        else:
            out_queue.appendleft(char)
            
    if not out_queue:
        return 0
    return ''.join(out_queue)


print(solution(n, cmds))