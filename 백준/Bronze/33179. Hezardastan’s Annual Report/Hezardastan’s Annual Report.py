n = int(input())
ps = list(map(int, input().split()))

val = 0
for p in ps:
    val += (p + 1) // 2

print(val)