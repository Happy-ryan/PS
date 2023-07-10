# https://www.acmicpc.net/problem/24509
from collections import defaultdict

n = int(input())
score_map = [list(map(int, input().split())) for _ in range(n)]
check = [0] * (n + 1)

for c in range(1, 5):
    score_dic = defaultdict()
    score = 0
    for r in range(n):
        score_dic[score_map[r][0]] = score_map[r][c]
        score = max(score, score_map[r][c])
        
    x = list(score_dic.items())
    x.sort(key= lambda x: x[0])
    x.sort(key= lambda x: x[1], reverse=True)
    
    for row in x:
        if check[row[0]] == 0:
            check[row[0]] = 1
            print(row[0], end=" ")
            break
        else:
            continue