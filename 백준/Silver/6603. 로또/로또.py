while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        num = arr.copy()[1:]
        visited = []
        idx = [0]
        used = [0] * len(num) # 중복허용불가

        def dfs(lev):
            if lev == 6:
                print(*visited)
                return
            for i in range(idx[-1], arr[0]):
                if used[i] == 0:
                    used[i] = 1
                    idx.append(i)
                    visited.append(num[i])
                    dfs(lev + 1)
                    used[i] = 0
                    visited.pop()
                    idx.pop()
    dfs(0)
    print()