R, G, B = map(int, input().split())

R_, G_, B_ = R / 255, G / 255, B / 255
K = 1 - max(R_, G_, B_)
if K == 1:
    C = M = Y = 0
else:
    C = (1 - R_ - K) / (1 - K)
    M = (1 - G_ - K) / (1 - K)
    Y = (1 - B_ - K) / (1 - K)

print(f"{C} {M} {Y} {K}")