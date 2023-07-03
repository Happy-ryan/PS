# https://www.acmicpc.net/problem/5557
# 시간복잡도 계산
# 2^98 > 2^10 = 10^3 > backtracking으로 전수조사 불가능함 > 시간초과
# dp로 memoizaion하면 메모리초과 무조건 발생
# > 딕셔너리로 다뤄야함.

from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

target = nums[-1]
nums = nums[:-1]


def check(n: int):
    return 0 <= n <= 20


dp = [Counter() for row in range(n)]
dp[1][nums[0]] = 1

for i in range(2, n):
    x = nums[i - 1]
    for num, add in dp[i - 1].items():
        plus_x = num + x
        minus_x = num - x

        if check(plus_x):
            dp[i][plus_x] += add
        if check(minus_x):
            dp[i][minus_x] += add

print(dp[-1][target])