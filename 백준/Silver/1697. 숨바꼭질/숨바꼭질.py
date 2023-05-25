n,m = map(int,input().split())

in_queue =[False]*100001
dist =[0]*100001

from collections import deque
q = deque([n])
in_queue[n] = True

while q:
    cur = q.popleft()
    num_list = [cur-1,cur+1,cur*2]
    for k in num_list:
        if 0<= k < 100001 and not in_queue[k]: # k를 먼저 판정해야지 index error가 안난다. in_queue 먼저 쓰면 index error 발생
            # k가 양수일 때만 해야함. 안그러면 0의 위치일 때 -1인덱스가 발생하게 된다.
            q.append(k)
            in_queue[k] = True
            dist[k] = dist[cur] + 1

print(dist[m])