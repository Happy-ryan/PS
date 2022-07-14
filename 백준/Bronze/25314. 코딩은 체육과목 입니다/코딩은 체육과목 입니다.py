n = int(input())
result = []
for _ in range(n//4):
    result.append('long')
result.append('int')
print(*result)
