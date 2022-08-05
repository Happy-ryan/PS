n = int(input())
arr = [input() for _ in range(n)]
# 뒤집힌 글자가 배열 안에 있는지 판단하는 함수
def f(arr):
    arr_set = set(arr)
    for row in arr_set:
        if row[::-1] in arr_set:
            return len(row), row[len(row)//2]
        

print(f(arr)[0],f(arr)[1])