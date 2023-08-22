t = int(input())
for _ in range(t):
    blank = input()
    num = int(input())
    sum = 0
    for i in range(num):
        x = int(input())
        sum += x
    print("YES" if sum%num == 0 else "NO")
