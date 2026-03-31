n = int(input())

participants = []

for i in range(1, n+1):
    s, c, l = map(int, input().split())
    participants.append((i, s, c, l))

participants.sort(key=lambda x: (-x[1], x[2], x[3]))

print(participants[0][0])