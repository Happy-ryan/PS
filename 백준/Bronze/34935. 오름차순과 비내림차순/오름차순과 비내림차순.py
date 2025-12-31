n = int(input())
nums = list(map(int, input().split()))

flag = True
for i in range(n - 1):
    if nums[i] >= nums[i + 1]:
        flag = False
        break

print(1 if flag else 0)
