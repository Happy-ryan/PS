from collections import Counter

def solution(w, k):
    
    dic = Counter(w)
    # k개 미만 문자는 제외.
    # 시간복잡도 O(len(w))
    for i in w:
        if i in dic and dic[i] < k:
            dic.pop(i)
    
    # 시간복잡도 O(len(w) + len(w))
    def find_word3(key):
        idxs = []
        for idx, i in enumerate(w):
            if i == key:
                idxs.append(idx)
                
        val = len(w) + 1
        for i in range(len(idxs) - k + 1):
            # print("1 :", idxs[i + k])
            # print("2 :", idxs[i])
            val = min(val, idxs[i + k - 1] - idxs[i] + 1)
            
        return val
    
    def find_word4(key):
        idxs = []
        for idx, i in enumerate(w):
            if i == key:
                idxs.append(idx)
                
        val = 0
        for i in range(len(idxs) - k + 1):
            # print("1 :", idxs[i + k])
            # print("2 :", idxs[i])
            if w[idxs[i + k - 1]] == w[idxs[i]]:
                val = max(val, idxs[i + k - 1] - idxs[i] + 1)
            
        return val
    
    
    inf = int(1e18)        
    max_val, min_val = -inf, inf
    # print(dic)
    for key in dic:
        # print("key:", key)
        val1 = find_word3(key)
        val2 = find_word4(key)
        # print('val1', val1)
        # print('val2', val2)
        max_val = max(max_val, val2)
        min_val = min(min_val, val1)
        # print("====")
        
    if max_val == -inf and min_val == inf:
        return -1
    return [min_val, max_val]

    
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    ans = solution(w, k)
    if ans == -1:
        print(ans)
    else:
        print(*ans)