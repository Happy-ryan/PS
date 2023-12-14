# 시간복잡도 O(len(num))
def f(n):
    if '7' not in str(n) and n % 7 != 0:
        return 0
    if '7' not in str(n) and n % 7 == 0:
        return 1
    if '7' in str(n) and n % 7 != 0:
        return 2
    if '7' in str(n) and n % 7 == 0:
        return 3

num = int(input())

result = f(num)
print(result)