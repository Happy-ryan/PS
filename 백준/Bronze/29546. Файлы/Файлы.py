n = int(input())
photos = [input() for _ in range(n)]

m = int(input())
for _ in range(m):
    l, r = map(int, input().split())
    for j in range(l - 1, r):
        print(photos[j])