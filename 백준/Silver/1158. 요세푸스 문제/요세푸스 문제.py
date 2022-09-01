from collections import deque
N,K = map(int,input().split())
q = deque(list(range(1,N+1)))
result = []
while len(result) != N:
    for x in range(K):
        if x < K-1:
            cur = q.popleft()
            q.append(cur)
        else:
            cur = q.popleft()
            result.append(cur)
s = ''
for i in range(len(result)):
    if i == len(result)-1:
        s += f"{result[i]}"
    else:
        s += f"{result[i]},"+' '
ss = '<'+s+'>'
print(ss)
