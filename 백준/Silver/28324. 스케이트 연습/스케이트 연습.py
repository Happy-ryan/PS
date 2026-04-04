n = int(input())
limits = list(map(int, input().split()))

# 마지막이 반드시 1
cnt = 0
val = 0
for i in range(n - 1, -1, -1):
    if i == n - 1:
        val = 1
    else:
        val = min(val + 1, limits[i]) # limit[i] 가 한계
        
    cnt += val
    
    # print(f"i: {i}, val: {val}, time: {cnt}")

time = cnt
print(time)