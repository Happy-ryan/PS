# https://www.acmicpc.net/problem/14627

S, C = map(int, input().split())
Ls = [int(input()) for _ in range(S)]
# target: 파의 길이
def get_count(target: int):
    cnt = 0
    for L in Ls:
        cnt += L // target
    return cnt

def binary_search():
    l, r = 1, 1000000001
    ans = 1
    while l <= r:
        m = (l + r) // 2
        if get_count(m) >= C:
            l = m + 1
            ans = m
        else:
            r = m - 1
    return ans

target = binary_search()
# ans = 0
# for L in Ls:
#     ans += L % target
    
ans = sum(Ls) - (target * C)
print(ans)
