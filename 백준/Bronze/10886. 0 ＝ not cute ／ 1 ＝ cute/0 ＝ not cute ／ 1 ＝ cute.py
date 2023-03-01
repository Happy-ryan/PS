t = int(input())
nums = [ input() for _ in range(t) ]
if nums.count('1') > nums.count('0'):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")  