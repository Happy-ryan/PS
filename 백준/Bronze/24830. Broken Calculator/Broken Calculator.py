memory_number = 1

n = int(input())

for _ in range(n):
    n1, cmd, n2 = input().split()
    
    n1 = int(n1)
    n2 = int(n2)
    
    if cmd == '+':
        ans = n1 + n2 - memory_number
    elif cmd == '-':
        ans = (n1 - n2) * memory_number
    elif cmd == '*':
        ans = (n1 * n2) ** 2
    else:
        if n1 % 2 == 0:
            ans = (n1) // 2
        else:
            ans = (n1 + 1) // 2
            
    print(ans)
    memory_number = ans