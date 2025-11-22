s = input().split("1")

max_zero = 0
for zeros in s:
    max_zero = max(max_zero, len(zeros))
    
# 0, 00 -> 1
# 000, 0000 -> 2

print((max_zero // 2) if max_zero % 2 == 0 else (max_zero // 2) + 1)
