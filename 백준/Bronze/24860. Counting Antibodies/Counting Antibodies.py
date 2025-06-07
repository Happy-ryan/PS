v1, j1 = map(int, input().split())
v2, j2 = map(int, input().split())
v3, d3, j3 = map(int, input().split())

val1, val2 = v1 * j1, v2 * j2
val3 = v3 * d3 * j3

print((val1 + val2) * val3)