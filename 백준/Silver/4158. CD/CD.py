from collections import deque

def solution(row_1, row_2):
    answer = 0
    
    while row_1 and row_2:
        if row_1[0] > row_2[0]:
            row_2.popleft()
        elif row_1[0] < row_2[0]:
            row_1.popleft()
        else:
            row_1.popleft()
            row_2.popleft()
            answer += 1
            
    return answer
        

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    row_1 = deque([int(input()) for _ in range(n)])
    row_2 = deque([int(input()) for _ in range(n)])
    print(solution(row_1, row_2))