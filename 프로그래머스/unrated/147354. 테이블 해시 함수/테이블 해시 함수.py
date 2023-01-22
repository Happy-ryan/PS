from functools import reduce

def f(row_idx, arr):
    cnt = 0
    for x in arr:
        cnt += x % row_idx
    return cnt

def solution(data, col, row_begin, row_end):
    answer = []
    r, c = len(data), len(data[0])
    # col 으로 정렬 ( 1정렬 )> 0번째 인덱스로 내림차순 정렬 ( 2정렬 )
    # 기준 두 개 쓸 때는 2정렬 후 1정렬 기입
    data.sort( key = lambda x : x[0], reverse = True)
    data.sort( key = lambda x : x[col - 1] )
    # print(data)
    for i in range(row_begin, row_end + 1):
        answer.append(f(i, data[i - 1]))
        
    ans = reduce( lambda x, y : x ^ y, answer)

    return ans