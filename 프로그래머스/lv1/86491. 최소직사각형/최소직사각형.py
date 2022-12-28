def solution(sizes):
    answer = 0
    # w h 구분없이 가장 긴 길이 찾기
    # w에 가장 긴 길이를 넣고 h로 조정하기
    w = 0
    for i in range(len(sizes)):
        for j in range(len(sizes[0])):
            w = max(w, sizes[i][j])
    h = 0
    for size in sizes:
        size_sort = sorted(size)[::-1]
        h = max(h,size_sort[1])
    
    return w * h