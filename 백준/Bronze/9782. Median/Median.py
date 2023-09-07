idx = 1
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = arr[0]
    if arr[0] % 2 == 0:
        avg = (arr[n//2] + arr[(n//2) + 1]) / 2
    else:
        avg = (arr[n//2 + 1])
    print(f"Case {idx}: {avg:.1f}")
    idx += 1