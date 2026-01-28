N, M = map(int, input().split())

cnt = N        # 지폐를 세는 횟수
bundle = N

while bundle >= M:
    bundle //= M
    cnt += bundle

print(cnt)