while True:
    s = input()
    if s == '#':
        break
    row = s.split()
    for a in row:
        print(a[::-1], end=' ')
    print()