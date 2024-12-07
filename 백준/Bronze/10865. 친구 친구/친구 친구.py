n, m = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(m)]

cnts = [0] * (n + 1)
for f in friends:
    a, b = f
    cnts[a] += 1
    cnts[b] += 1
    
for x in cnts[1:]:
    print(x)