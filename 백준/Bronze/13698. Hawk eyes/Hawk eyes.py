moves = input()

small = 1
big = 4

for m in moves:
    if m == 'A':
        x, y = 1, 2
    elif m == 'B':
        x, y = 1, 3
    elif m == 'C':
        x, y = 1, 4
    elif m == 'D':
        x, y = 2, 3
    elif m == 'E':
        x, y = 2, 4
    elif m == 'F':
        x, y = 3, 4

    if small == x:
        small = y
    elif small == y:
        small = x

    if big == x:
        big = y
    elif big == y:
        big = x

print(small)
print(big)