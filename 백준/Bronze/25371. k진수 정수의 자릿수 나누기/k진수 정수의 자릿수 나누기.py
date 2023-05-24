# https://www.acmicpc.net/problem/25371


# 10진수 n을 m진수로 변경하는 함수
def conv(n, m):
    if n == 0:
        return 0
    
    res = ""
    conv = "0123456789abcdef"
    while n > 0:
        n, mod = divmod(n, m)
        res += conv[mod]
        
    return res[::-1]

    
def solution(num:str):
    nums = num.split("0")
    sum_val = 0
    for x in nums:
        if x.isdigit():
            sum_val += int(x)
    return conv(sum_val, m)


n, m = map(int, input().split())
x = conv(n, m)
y = solution(x)

print(y)