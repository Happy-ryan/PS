a, b, c = map(int, input().split())

cmds = ['+', '-', '*', '/']

for cmd in cmds:
    if cmd == '+':
        if a + b == c:
            print(f"{a}+{b}={c}")
        elif a == b + c:
            print(f"{a}={b}+{c}")
    elif cmd == '-':
        if a - b == c:
            print(f"{a}-{b}={c}")
        elif a == b - c:
            print(f"{a}={b}-{c}")
    elif cmd == '*':
        if a * b == c:
            print(f"{a}*{b}={c}")
        elif a == b * c:
            print(f"{a}={b}*{c}")
    elif cmd == '/':
        if a // b == c:
            print(f"{a}/{b}={c}")
        elif a == b // c:
            print(f"{a}={b}/{c}")