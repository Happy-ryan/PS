i = 1
while True:
    x, cmd, y = input().split()
    x = int(x)
    y = int(y)
    if cmd == 'E':
        break
    if cmd == '>':
        print(f"Case {i}: {'true' if (x > y) == True else 'false'}")
    elif cmd == '>=':
        print(f"Case {i}: {'true' if (x >= y) == True else 'false'}")
    elif cmd == '<':
        print(f"Case {i}: {'true' if (x < y) == True else 'false'}")
    elif cmd == '<=':
        print(f"Case {i}: {'true' if (x <= y) == True else 'false'}")
    elif cmd == '==':
        print(f"Case {i}: {'true' if (x == y) == True else 'false'}")
    elif cmd == '!=':
        print(f"Case {i}: {'true' if (x != y) == True else 'false'}")
    i += 1