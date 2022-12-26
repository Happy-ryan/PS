def solution(arr):    
    if len(arr) == 1:
        return [-1]
    else:
        idx = arr.index(min(arr))
        del arr[idx]
        return arr

