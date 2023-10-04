# https://www.acmicpc.net/problem/21567
from collections import Counter
n = 3
nums = [int(input()) for _ in range(n)]

def cnt_num(nums):
    num = 1
    for x in nums:
        num *= x
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in str(num):
        result[int(x)] += 1
    return result


for x in cnt_num(nums):
    print(x)