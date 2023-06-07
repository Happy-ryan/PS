# https://www.acmicpc.net/problem/2592
from collections import Counter

arr = [int(input()) for row in range(10)]

def solution(arr:list):
    arr = Counter(arr)
    max_fre = max([value for value in arr.values()])
    sum_val = 0
    fre_ = 0
    for key, value in arr.items():
        sum_val += key * value
        if value == max_fre:
            fre_ = key
            
    mean_ = sum_val // 10
    return mean_, fre_

print(solution(arr)[0])
print(solution(arr)[1])