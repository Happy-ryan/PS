n = int(input())
nums = [int(input()) for _ in range(n)]
print(sum(1 for x in nums if x % 2 != 0))