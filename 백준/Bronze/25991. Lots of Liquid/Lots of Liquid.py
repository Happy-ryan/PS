n = int(input())
nums = list(map(float,input().split()))

val = 0
for x in nums:
    val += x ** 3
print(val ** (1/3))
