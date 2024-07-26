n = int(input())
dirs = list(map(int, input().split()))

total_sum = sum(dirs)

if total_sum > 0:
    print('Right')
elif total_sum < 0:
    print('Left')
else:
    print('Stay')