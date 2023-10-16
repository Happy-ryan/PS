# https://www.acmicpc.net/problem/27172
# 시간복잡도 : 이중포문 - 100 000 * 100 000 = 10^10 > 시간초과
# 내가 얻은 카드 숫자의 약수가 다른 사람에게 있는지 없는지 판단하는게 포인트!
from collections import Counter

def get_divisors(num):
    divisors = set()
    sqrt_num = int(num ** 0.5) + 1
    for i in range(1, sqrt_num):
        if num % i == 0:
            divisors.add(i)
            if i != 1 and i != num // i:
                divisors.add(num // i)
    return divisors

n = int(input())
nums = list(map(int, input().split()))

dic = {}
for num in nums:
    dic[num] = get_divisors(num)
    
scores = [0] * n

divisor_counter = Counter()
for key, value in dic.items():
    for div in value:
        # dict에서 in은 key를 순회함. 시간복잡도는 set의 in과 동일함.
        if div in dic:
            divisor_counter[div] += 1
            divisor_counter[key] -= 1

for idx, num in enumerate(nums):
    scores[idx] = divisor_counter[num]

print(*scores)
