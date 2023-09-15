p1, p2 = 100, 100

def verseScore(score1, score2):
    global p1, p2
    if score1 > score2:
        p2 -= score1
    elif score1 < score2:
        p1 -= score2

n = int(input())

for _ in range(n):
    score1, score2 = map(int, input().split())
    verseScore(score1, score2)

print(p1)
print(p2)