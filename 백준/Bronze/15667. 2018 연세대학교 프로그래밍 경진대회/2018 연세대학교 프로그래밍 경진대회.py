n = int(input())

# 폭죽 1개 -> 대형 불꽃 1개 -> 중형 불꽃 1 * K 개 -> 소형 불꽃 1 * K * K 개
# 총 불꽃의 수 = K * K + K + 1 = K (K + 1) + 1

n -= 1
for k in range(1, 101):
    if k * (k + 1) == n:
        print(k)
        break