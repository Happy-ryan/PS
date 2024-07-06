t = int(input())

for i in range(t):
    num = int(input())
    cmds = input()
    for cmd in cmds:
        if cmd == 'b':
            num -= 1
        else:
            num += 1
        
        if num == 0:
            break
    print(f'Data Set {i + 1}:')
    print(num)
    print()