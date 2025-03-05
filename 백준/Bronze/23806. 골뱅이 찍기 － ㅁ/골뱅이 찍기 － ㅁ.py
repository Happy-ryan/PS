n = int(input())

for _ in range(n):
    for _ in range(5 * n):
        print('@', end = '')
    print()
    
for _ in range(3 * n):
        print('@' * n + ' ' * 3 * n + '@' * n)
        
for _ in range(n):
    for _ in range(5 * n):
        print('@', end = '')
    print()
