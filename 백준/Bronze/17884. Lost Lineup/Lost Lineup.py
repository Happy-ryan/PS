n = int(input())
d = list(map(int, input().split()))

line = [0] * n
line[0] = 1 

for i in range(1, n):
    pos = d[i - 1] + 1
    line[pos] = i + 1

print(*line)
