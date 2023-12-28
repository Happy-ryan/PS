N, K = map(int, input().split())
times = list(map(int, input().split()))

def get_ballon(times, target):
    ballons = 0
    for time in times:
        ballons += target // time
    return ballons


def binary_search():
    #l, r: 시간, 자연수
    l, r = 1, 10**(12) + 1
    ans = 0
    while l <= r:
        m = (l + r) // 2
        if get_ballon(times, m) >= K:
            r = m - 1
            ans = m
        else:
            l = m + 1
    
    return ans


print(binary_search())