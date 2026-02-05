idx = 1
while True:
    s = input()
    if s == 'Was it a cat I saw?':
        break
    for i in range(0, len(s), idx + 1):
        print(s[i], end='')
    print()
    idx += 1