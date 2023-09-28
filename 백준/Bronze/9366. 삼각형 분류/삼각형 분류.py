t = int(input())

for num in range(t):
    arr = sorted(map(int, input().split()))
    prefix = f"Case #{num+1}:"
    if arr[0] + arr[1] <= arr[2]:
        print(f"{prefix} invalid!")
    elif arr[0] == arr[1] == arr[2]:
        print(f"{prefix} equilateral")
    elif (arr[0] == arr[1]) or (arr[1] == arr[2]) or (arr[2] == arr[0]):
        print(f"{prefix} isosceles")
    else:
        print(f"{prefix} scalene")