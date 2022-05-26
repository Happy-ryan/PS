N = int(input())
arr = [input() for _ in range(N)]
if arr == sorted(arr):
    print("INCREASING")
elif sorted(arr) ==arr[::-1]:
    print("DECREASING")
else:
    print("NEITHER")