n = int(input())
nums = [list(map(int, input().split())) for _ in range(3)]

def solution(n, nums):
    cnt = 0

    for num in nums:
        if 7 in num:
            cnt += 1

    if cnt >= 3:
        return 777
    return 0

print(solution(n, nums))