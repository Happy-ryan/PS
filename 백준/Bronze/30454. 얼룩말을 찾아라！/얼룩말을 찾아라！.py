n, l = map(int, input().split())

hs = [input() for _ in range(n)]


dic = {}
max_cnt = 0
for idx, h in enumerate(hs):
    h = h.split('0')
    cnt = len(h) - h.count('')
    dic[idx] = cnt
    max_cnt = max(max_cnt, cnt)
    
result = 0
for key, value in dic.items():
    if value == max_cnt:
        result += 1
    

print(max_cnt, result)