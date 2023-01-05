
T = int(input())
score = [0] + [int(input()) for _ in range(T)]
score.sort()
cnt = 0
for i in range(1, T + 1):
    cnt += abs(i - score[i])
print(cnt)