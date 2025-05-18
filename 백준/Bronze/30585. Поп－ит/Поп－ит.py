n, m = map(int, input().split())

cnt1 = 0
cnt2 = 0

for _ in range(n):
    a = input()
    cnt1 += a.count('0')
    cnt2 += a.count('1')

print(min(cnt1, cnt2))