# https://www.acmicpc.net/problem/17614

def f(num:int) -> int:
    num = str(num)
    l = len(num)
    num = num.replace('3','')
    num = num.replace('6','')
    num = num.replace('9','')
    return l - len(num)


n = int(input())
cnt = 0
for num in range(1, n + 1):
    cnt += f(num)
print(cnt)
    