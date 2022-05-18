N,M = map(int, input().split())
arr = [ input().split() for _ in range(N)]
brr = [input() for _ in range(M)]
arr_dict = dict(arr)
for row in brr:
    print(arr_dict[row])