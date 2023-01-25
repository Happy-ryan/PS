t = int(input())
for _ in range(t):
    num, s = list(input().split())
    num = int(num)
    s = list(s)
    s[num - 1] = ''
    print(''.join(s))