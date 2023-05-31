# https://www.acmicpc.net/problem/11655

def getDivisor(num: int):
    ans = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            ans.append(i)
            if i * i != num:
                ans.append(num // i)
    ans.sort()
    ans.pop()
    if sum(ans) != num:
        return f'{num} is NOT perfect.'
    else:
        return f'{num} = {(" + ".join(map(str, ans)))}'
    
    
while True:
    num = int(input())
    if num == -1:
        break
    print(getDivisor(num))