N, M = map(int, input().split())

total = (M * 1440) // N  
h = total // 60
m = total % 60

print(f"{h:02d}:{m:02d}")
