n = int(input())
nums = list(map(int, input().split()))

cnt1, cnt2 = 0, 0

for num in nums:
    if num % 2 != 0:
        cnt1 += 1
    else:
        cnt2 += 1
        
if cnt2 > cnt1:
    print("Happy")
else:
    print('Sad')