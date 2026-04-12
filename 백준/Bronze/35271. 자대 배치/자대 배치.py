N, M = map(int, input().split())
candis = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(N)]

answer = []

for idx, info in enumerate(infos):
    a, b, c = info
    a -= 1
    b -= 1
    c -= 1
    if candis[a] > 0:
        candis[a] -= 1
        answer.append((idx + 1, a + 1))
    elif candis[b] > 0:
        candis[b] -= 1
        answer.append((idx + 1, b + 1))
    elif candis[c] > 0:
        candis[c] -= 1
        answer.append((idx + 1, c + 1))
    else:
        answer.append((idx + 1, -1))
        

for row in answer:
    print(row[1], end = ' ')