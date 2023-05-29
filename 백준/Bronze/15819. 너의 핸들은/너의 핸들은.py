n, m = map(int, input().split())
arr = [input() for row in range(n)]
arr.sort()
arr = [0] + arr
print(arr[m])