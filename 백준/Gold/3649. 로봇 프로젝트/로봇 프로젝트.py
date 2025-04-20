# 구멍의 너비 x = 두 조각의 길이의 합 
def solution(x, n, pieces):
    x *= 10000000
    # 정렬해도 상관없음
    pieces.sort()

    # x = l + r
    # l이 커지면 r이 줄어야함.
    # 즉 l, r은 다른 방향 이동 필요.
    # l 고정, r 이동
    r = n - 1
    for  l in range(n):
        while l + 1 < r and pieces[l] + pieces[r] > x:
            r -= 1
        
        if l != r and pieces[l] + pieces[r] == x:
            return ['yes', pieces[l], pieces[r]]
    
    return ['danger']

while True:
    try:
        x = int(input())
        n = int(input())
        pieces = [int(input()) for _ in range(n)]
        print(*solution(x, n, pieces))
    except:
        break