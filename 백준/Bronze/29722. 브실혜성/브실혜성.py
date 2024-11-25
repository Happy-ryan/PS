y, m, d = map(int, input().split('-'))
n = int(input())
# 0base
total = (d - 1) + (m - 1) * 30 + y * 30 * 12
total += n

year = total // (30 * 12)
total %= (30 * 12) 
month = total // 30
month += 1 #1base
total %= 30
day = total
day += 1 #1base

print(f'{year}-{month:02}-{day:02}')