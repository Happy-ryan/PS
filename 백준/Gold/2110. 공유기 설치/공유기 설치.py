N,C= map(int, input().split())
arr= [ int(input()) for _ in range(N)]
arr = sorted(arr)
# print(arr)
def f(x): # f(X): 최소거리x일때 설치할 수 있는 공유기의 개수
    s,e = 0,0
    cnt = 1 # 처음은 무조건 설치
    while e < len(arr):
        if arr[e]-arr[s] >= x: 
            s = e
            e +=1
            cnt +=1 #최소거리보다 크거나 같으면 설치가능하다.
        else :
            e+=1
    return cnt

l,r = 1, max(arr)-min(arr)+1
while r-l != 1:
    m = (l+r)//2
    if f(m) >= C:
        l = m
    else : r = m
print(l)