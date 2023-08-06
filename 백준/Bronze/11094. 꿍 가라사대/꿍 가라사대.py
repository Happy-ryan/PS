t = int(input())
for _ in range(t):
    s = input()
    if 'Simon says' in s:
        s = s.replace('Simon says', '')
        print(s)