t = int(input())

def solutino(nums):
    cnt = 0
    for num in nums:
        if num >= 10:
            cnt += 1
    return cnt

for _ in range(t):
    nums = list(map(int, input().split()))
    cnt = solutino(nums)
    print(*nums)
    if cnt >= 3:
        print('triple-double')
    elif cnt >= 2:
        print('double-double')
    elif cnt >= 1:
        print('double')
    else:
        print('zilch')
    print()