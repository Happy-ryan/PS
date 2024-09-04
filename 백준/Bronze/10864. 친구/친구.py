n, m = map(int, input().split())

friends = [list(map(int, input().split())) for _ in range(m)]
sum_val = [0] * (n + 1)

for friend in friends:
    a, b = friend
    sum_val[a] += 1
    sum_val[b] += 1
    
for x in sum_val[1:]:
    print(x)