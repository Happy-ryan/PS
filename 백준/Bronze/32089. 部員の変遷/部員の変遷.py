while True:
    cnt = 0
    n = int(input())
    if n == 0:
        break
    nums = list(map(int, input().split()))
    for x in range(n - 3 + 1):
        cnt = max(cnt, sum(nums[x : x + 3]))
    
    print(cnt)