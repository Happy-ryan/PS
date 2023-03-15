# 각 자리수의 합 더하기(DigitSum)
# n : 10진수 , k진법의 각 자리수의 합
def DigitSum(n, k):
    sum_val = 0

    while n >= k:
        sum_val += n % k
        n //= k
    sum_val += n

    return sum_val


for num in range(1000, 10000):
    if DigitSum(num, 10) == DigitSum(num, 12) == DigitSum(num, 16):
        print(num)
