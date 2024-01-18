n = int(input())
scores = list(map(int, input().split()))
scores.sort()
x, y = map(int, input().split())

상대 = n * x // 100
절대 = sum([1 for x in scores if x >= y])

print(상대, 절대)