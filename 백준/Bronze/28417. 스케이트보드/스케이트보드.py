n = int(input())

ans = 0
for _ in range(n):
    scores = list(map(int, input().split()))
    one = max(scores[0], scores[1])
    two, three = sorted(scores[2:])[-1], sorted(scores[2:])[-2]
    ans = max(ans, one + two + three)

print(ans)