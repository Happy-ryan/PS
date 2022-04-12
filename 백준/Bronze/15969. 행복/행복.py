N = int(input())
score=list(map(int, input().split()))

min_score = min(score)
max_score = max(score)

print(max_score-min_score)