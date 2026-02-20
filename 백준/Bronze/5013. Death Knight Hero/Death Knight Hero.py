n = int(input())

wins = 0

for _ in range(n):
    s = input().strip()
    if "CD" not in s:
        wins += 1

print(wins)