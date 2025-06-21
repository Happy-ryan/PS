n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    

    cnt = 1
    
    for i in range(n - 1):
        if arr[i] <= arr[i+1]:
            cnt += 1

            
    return cnt


print(solution(n, arr))