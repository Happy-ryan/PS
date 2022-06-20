while True:
    arr = list(map(int, input().split()))
    if arr[0]==0:
        break
    else:
        arr = arr[1:]
        result = [arr[0]]
        for x in arr:
            if x == result[-1]: # 있는 것은 넣지 않는다. append하기 때문에 새로운 요소는 반드시 -1인덱스를 갖는다.
                continue
            else: result.append(x)
        result.append('$')
        print(*result)