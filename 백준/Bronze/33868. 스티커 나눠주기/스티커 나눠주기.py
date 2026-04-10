n = int(input())

max_T = 0
min_B = float('inf')

for _ in range(n):
    T, B = map(int, input().split())
    max_T = max(max_T, T)
    min_B = min(min_B, B)

value = max_T * min_B

print((value % 7) + 1)