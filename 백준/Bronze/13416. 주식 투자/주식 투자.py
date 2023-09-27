T = int(input())
for _ in range(T):
    N = int(input())
    ans = 0
    for i in range(N):
        stocks = list(map(int, input().split()))
        if max(stocks) >= 0:
            ans += max(stocks)
    print(ans)