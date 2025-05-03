n = int(input())

cnt = 0
for _ in range(n):
    x = input()
    cnt += 1 if x[0] == 'C' else 0

print(cnt)