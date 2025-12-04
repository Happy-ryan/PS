t = int(input())

for case in range(t):
    num, ch = input().split()
    num = int(num)
    start = ord(ch)

    for i in range(1, num + 1):
        # 현재 문자
        cur = chr((start - ord('A') + (i - 1)) % 26 + ord('A'))
        print(cur * i)

    if case != t - 1:
        print()
