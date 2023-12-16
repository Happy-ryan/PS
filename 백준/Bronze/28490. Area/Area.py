n = int(input())
max_val = 0
for _ in range(n):
    a, b = map(int, input().split())
    max_val = max(a * b, max_val)
    
print(max_val)