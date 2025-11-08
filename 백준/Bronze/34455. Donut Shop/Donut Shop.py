D = int(input())
E = int(input())

for _ in range(E):
    cmd = input()
    q = int(input())
    if cmd == '+':
        D += q
    elif cmd == '-':
        D -= q
        
print(D)