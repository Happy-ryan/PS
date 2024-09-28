t = int(input())

def solution(n: int):
    # 목표: 2 ~ 64 진법으로 변경되었을 때 회문이 될 수 있는가?

    # 1. 10진법 n -> m(2 ~ 64)진법으로 변경
    def conv(n: int, m: int) -> str:
        if n == 0:
            return 0
        # 10 + 26 + 26 + 2 = 64
        conv = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@"
        ans = ""
        while n > 0:
            n, mod = divmod(n, m)
            ans += conv[mod]
        return ans[::-1]
    
    # 2. 회문인지 파악
    def is_palindrom(x: str):
        k = len(x)
        for i in range(k // 2):
            if x[i] != x[k - i- 1]:
                return False
        return True

    flag = False
    for m in range(2, 65):
        res = conv(n, m)
        if is_palindrom(res):
            flag = True
    
    if flag:
        return 1
    return 0

for _ in range(t):
    x = int(input())
    print(solution(x))