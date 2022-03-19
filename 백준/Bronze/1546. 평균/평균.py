N = int(input())
score = list(map(float, input().split()))
max_score = max(score)
newsum = 0
for i in score :
    new_score = (i/max_score) * 100
    newsum += new_score
print(round(newsum/N, 2))