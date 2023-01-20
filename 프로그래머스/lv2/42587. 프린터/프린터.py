from collections import deque

def check(p, q): # 내 뒤에 나보다 큰 우선순위가 있니?
    flag = True
    for i in range(len(q)):
        if p < q[i][1]:
            flag = False
    return flag

def solution(priorities, location):
    answer = deque([])
    q = deque([])
    for idx, p in enumerate(priorities):
        q.append((idx, p))
    while q:
        idx, p = q.popleft()
        if check(p, q):
            answer.append((idx, p))
        else:
            q.append((idx, p))
    
    for i in range(len(answer)):
        if answer[i][0] == location:
            return i + 1
