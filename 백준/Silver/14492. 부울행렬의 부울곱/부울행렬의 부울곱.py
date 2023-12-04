def matix_dot(board1, board2):
    i, k = len(board1), len(board1[0])
    k, j = len(board2), len(board2[0])
    result = [[0 for col in range(j)] for row in range(i)]
    
    for i_ in range(i):
        for j_ in range(j):
            ans = set()
            for k_ in range(k):
                result[i_][j_] = result[i_][j_] | (board1[i_][k_] & board2[k_][j_])
    return result

n = int(input())
board1 = [list(map(int, input().split())) for _ in range(n)]
board2 = [list(map(int, input().split())) for _ in range(n)]
result = matix_dot(board1,board2)

cnt = 0
for row in result:
    cnt += row.count(1)
    
print(cnt)