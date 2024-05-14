n, m = map(int, input().split())
board1 = [list(input()) for _ in range(n)]
input()
board2 = [list(input()) for _ in range(n)]

def solution(n, m, board1, board2):
    answer = 0
    for r in range(n):
        for c in range(m):
            if board1[r][c] == board2[r][c]:
                answer += 1
                
    return answer


print(solution(n, m, board1, board2))