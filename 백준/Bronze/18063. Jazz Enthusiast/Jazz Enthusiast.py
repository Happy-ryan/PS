n, c = map(int, input().split())

total_second = 0

for _ in range(n):
    m, s = input().split(":")
    total_second += int(m) * 60 + int(s)

total_second -= c * (n - 1)

hours = total_second // 3600
total_second %= 3600
minutes = total_second // 60
seconds = total_second % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")