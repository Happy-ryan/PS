ret = []
for _ in range(5) :
    arr = list(map(int, input().split(" ")))
    ret.append(sum(arr))

result = max(ret)
result_idx = ret.index(result) + 1

print(result_idx, result)