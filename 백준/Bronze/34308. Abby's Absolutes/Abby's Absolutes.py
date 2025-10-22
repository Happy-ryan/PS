N, K = map(int, input().split())
wants = list(map(int, input().split()))

result = []
for x in wants:
    if abs(x - 1) < abs(x - N):
        result.append(1)
    elif abs(x - 1) > abs(x - N):
        result.append(N)
    else:
        result.append(1)

print(*result)