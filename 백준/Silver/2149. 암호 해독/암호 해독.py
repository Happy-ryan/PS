from copy import deepcopy
# 키와 암호문(after) > 평문(before) 추론!!
key = list(input())
origin_key = deepcopy(key)
after = list(input())

# 키 정렬
key.sort()
# 정렬 후 바뀐 인덱스의 원래 인덱스 값이 얼마인가?
# 같은 문자가 나왔을 때 인덱스에 문제가 발생함!
# index, find로 구하지 않고 직접 구함!
origin_index = []
for k in key:
    for idx, ok in enumerate(origin_key):
        if k == ok and idx not in origin_index:
            origin_index.append(idx)
# 정렬 후 바뀌 인덱스0의 원래 인덱스는 3이다! - 예시기준
w, h = len(key), len(after) // len(key)
memo = [['' for _ in range(w)] for _ in range(h)]
idx = 0
for j in range(w):
    for i in range(h):
        memo[i][j] = after[idx]
        idx += 1
        
org_memo = [['' for _ in range(w)] for _ in range(h)]
for r in range(h):
    for pre_idx, org_index in enumerate(origin_index):
        org_memo[r][org_index] = memo[r][pre_idx]
    
for i in range(h):
    for j in range(w):
        print(org_memo[i][j], end='')