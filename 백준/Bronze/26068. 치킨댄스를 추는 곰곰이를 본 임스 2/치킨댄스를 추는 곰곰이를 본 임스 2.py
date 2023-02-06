t = int(input())
cnt = 0
for _ in range(t):
    D, num = input().split('-')
    num = int(num)
    if num <= 90:
        cnt += 1
print(cnt)