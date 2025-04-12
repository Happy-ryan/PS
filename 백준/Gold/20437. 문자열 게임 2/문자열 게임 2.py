from collections import Counter

def solution(w, k):
    
    dic = Counter(w)
    # k개 미만 문자는 제외.
    # 시간복잡도 O(len(w))
    for i in w:
        # dic 쓸 때 pop 쓰면 key 사라질 수 있음..매우 주의!!
        if i in dic and dic[i] < k:
            dic.pop(i)
    
    # 시간복잡도 O(len(w) + len(w))
    def find_word3(key):
        idxs = []
        for idx, i in enumerate(w):
            if i == key:
                idxs.append(idx)
                
        min_val, max_val = len(w), -len(w)
        for i in range(k - 1, len(idxs)):
            l, r = i - k + 1, i
            min_val = min(min_val, idxs[r] - idxs[l] + 1)
            max_val = max(max_val, idxs[r] - idxs[l] + 1)
            
        return min_val, max_val
    
    
    inf = int(1e18)        
    max_val, min_val = -inf, inf
    for key in dic:
        val1, val2 = find_word3(key)
        max_val = max(max_val, val1, val2)
        min_val = min(min_val, val1, val2)
        
    if max_val == -inf and min_val == inf:
        return [-1]
    return [min_val, max_val]

    
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    ans = solution(w, k)
    print(*ans)