arr = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    arr = arr[:a] + arr[a: b + 1][::-1] + arr[b + 1:]

print(*arr)