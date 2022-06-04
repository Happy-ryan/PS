N = int(input())
arr = [int(input()) for _ in range(N)]
cnt = sum(arr) - (len(arr) -1)
print(cnt)