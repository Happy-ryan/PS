# https://www.acmicpc.net/problem/12760
N, M = map(int, input().split())
cards = [list(reversed(sorted(list(map(int, input().split()))))) for _ in range(N)]

scores = [0] * N
for c in range(M):
    max_score = 0
    for r in range(N):
        max_score = max(cards[r][c], max_score)
    for k in range(N):
        if cards[k][c] == max_score:
            scores[k] += 1

max_cnt = max(scores)
for idx, score in enumerate(scores):
    if score == max_cnt:
        print(idx + 1, end= " ")