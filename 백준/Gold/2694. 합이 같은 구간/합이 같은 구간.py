t = int(input())

def solution(n, old):
    
    arr = []
    for row in old:
        arr.extend(row)
    
    def get_divisor(n):
        res = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(i)
                if i * i != n:
                    res.append(n // i)
        res.sort()
        return res
    
    psum = [0] * (n + 1)
    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + arr[i - 1]
    
    S = sum(arr)
    # print(f"arr: {arr}")
    res = get_divisor(S)
    # print(f"약수 : {res}")
    psum = psum[1:]
    # print(f"psum : {psum}")
    
    
    def cal(mod):
        idxs = []
        for idx, p in enumerate(psum):
            if p % mod == 0:
                idxs.append(idx)
        
        if len(idxs) == (S // mod):
            return True
        return False
    
    val = S
    for i in res:
        if cal(i):
            val = min(val, i)
            
    return val
            
for _ in range(t):
    n = int(input())
    n_ = (n // 10) + 1 if n % 10 != 0 else n // 10
    arr = [list(map(int, input().split())) for _ in range(n_)]
    print(solution(n, arr))