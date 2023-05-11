#https://www.acmicpc.net/submit/16546
n = int(input())
nums = set(map(int, input().split()))
all = set(list(range(1, n + 1)))
print(*(all - nums))