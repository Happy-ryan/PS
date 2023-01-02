# 10진법N을 M진법으로 변환
def f(N, M, r):
    res = ''
    while N > 0:
        N, mod = divmod(N, M)
        res += str(mod)
    # 정사각형의 한 변의 길이 r로 맞추기 위해서 조정
    x = r - len(res)
    if x == 0:
        return res[::-1]
    else:
        return '0' * x + res[::-1]

def solution(n, arr1, arr2):
    answer = [[0 for col in range(n)] for row in range(n)]
    for r in range(n):
        for c in range(n):
            if f(arr1[r],2,n)[c] == '1' or f(arr2[r],2,n)[c] == '1':
                answer[r][c] = '#'
            else:
                answer[r][c] = ' '
    
    res = []
    for row in answer:
        print(*row)
        res.append(''.join(row))
    return res