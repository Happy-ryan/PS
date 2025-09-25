n = int(input())

for _ in range(4 * n):
    for _ in range(n):
        print("@", end='')
    print()
    
for _ in range(n):
    for _ in range(n * 5):
        print("@", end='')
    print()