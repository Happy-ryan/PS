n = int(input())
votes = [int(input()) for _ in range(n)]
print('S' if votes[0] >= max(votes) else 'N')