N, M = map(int, input().split())
arr = list(map(int,input().split()))

def f(h): # 절단기의 높이가 h일 때 가져갈 수 있는 나무의 총 길이
    cnt = 0
    for i in arr:
        if i >= h:
            cnt += (i-h)
    return cnt

l,r = -1, int(1e12) # l과 r은 절단기의 높이 : r 리턴을 하는데 범위를 보면 r은 절단기의 높이이므로 0~max(arr)이 된다.
                  # 따라서 l의 범위는 -1~max(arr)-1
while r-l != 1:
    m = (r+l)//2
    if f(m) >= M: # 이렇게 하는 이유 f(h)의 값에 원하는 M이 없을 수 있다. 그러면 조금 더 가져가는게 맞다. 따라서
                  # l을 리턴해 lower_bound를 출력하면 딱 떨어지게 가져가거나 조금 더 가져가게 된다.
        l = m
    else : r = m
print(l)
