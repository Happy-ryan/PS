N, A = map(int, input().split())
costs = list(map(int, input().split()))
val = 0
for cost in costs:
    val += cost // A
print(val)