n = input().rstrip()

if n[0] == '0' and n[1] != 'x':
    print(int(n, 8))
elif n[0] == '0' and n[1] == 'x':
    print(int(n[2:], 16))
else:
    print(n)