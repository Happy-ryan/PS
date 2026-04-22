MOD = 14579

a, b = map(int, input().split())

result = 1

for n in range(a, b + 1):
    term = n * (n + 1) // 2
    result = (result * term) % MOD # 곱할때마다 모듈러

print(result)