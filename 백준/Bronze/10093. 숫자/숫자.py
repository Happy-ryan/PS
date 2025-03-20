a, b = map(int, input().split())

x1 = min(a, b)
x2 = max(a, b)

if x2 - x1 - 1 <= 0:
    print(0)
else:
    print(x2 - x1 - 1)
    
for x in range(x1 + 1, x2):
    print(x, end = ' ')