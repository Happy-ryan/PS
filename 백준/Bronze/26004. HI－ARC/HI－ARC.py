n = int(input())
from collections import Counter
arr = Counter(list(input()))

def make():
    cnt = 0
    for x in 'HIARC':
        if arr[x] != 0:
            cnt += 1
            arr[x] -= 1
        else:
            return 0
    return 1

cnt = 0
while True:
    if make():
        cnt += 1
    else:
        print(cnt)
        break