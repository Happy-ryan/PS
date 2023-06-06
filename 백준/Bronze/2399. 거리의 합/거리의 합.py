# https://www.acmicpc.net/problem/2399

def solution(arr:list):
    sum_val = 0
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)): 
            sum_val += abs(arr[i] - arr[j])
    return sum_val * 2

t = int(input())
arr = list(map(int, input().split()))
print(solution(arr))