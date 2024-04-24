n = int(input())
arr = list(map(int, input().split()))

def solution(n, arr):
    # 시간복잡도 O(N)
    max_num = max(arr)
    max_idx = arr.index(max_num)

    flag = True
    start = arr[0]
    for i in range(1, max_idx + 1):
        if start < arr[i]:
            start = arr[i]
        else:
            flag = False
            
    for i in range(max_idx + 1, n):
        if start > arr[i]:
            start = arr[i]
        else:
            flag = False
            
    if flag:
        return 'YES'
    else:
        return 'NO'
    
print(solution(n, arr))