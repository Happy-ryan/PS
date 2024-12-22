n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def solution(n, arr):
    # 정렬 : 문제 개수 -> 패널티 총합
    arr.sort(key = lambda x : (-x[0], x[1]))   
    
    five = arr[4][0]
    cnt = 0
    for row in arr[5:]:
        score, _ = row
        if score == five:
            cnt += 1
    return cnt
    
print(solution(n, arr))