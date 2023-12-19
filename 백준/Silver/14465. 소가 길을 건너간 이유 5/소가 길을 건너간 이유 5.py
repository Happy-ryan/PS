n, k, b = map(int, input().split())
broken = set([int(input()) for _ in range(b)])
nums = list(range(n + 1))

# 0 1 2 3 4 5 6 7 8 9 10
#   # #     #       #  #
# l = 1, r = 4
# 한 옆으로 움직이면 기존의 l은 빠지고 새로운 r이 들어온다.
# 새로운 l은 이미 기존의 범위에 포함이 되었기 때문에 고려할 필요 없고
# 기존 r은 이미 기존의 범위에 포함이 되었기 때문에 고려할 필요 없다.

cnt = 0
l = 1
r = l + k - 1
for x in broken:
    if l <= x <= r:
        cnt += 1

ans = 100001
while r < n:
    if nums[l] in broken:
        cnt -= 1
    l += 1
    r += 1
    if nums[r] in broken:
        cnt += 1
    ans = min(ans, cnt)
    
print(ans)