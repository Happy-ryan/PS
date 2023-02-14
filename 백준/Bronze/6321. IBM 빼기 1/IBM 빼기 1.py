t = int(input())
for i in range(1,t + 1):
    s = input()
    ans = ''
    for x in s:
        if x == 'Z':
            ans += 'A'
        else:
            ans += chr(ord(x) + 1)
    print(f"String #{i}")
    print(ans)
    print()
