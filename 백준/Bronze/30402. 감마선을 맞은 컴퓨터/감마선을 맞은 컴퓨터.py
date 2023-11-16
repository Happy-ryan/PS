def f(arr):
    for row in arr:
        if 'w' in row:
            return "chunbae"
        if 'b' in row:
            return 'nabi'
        if 'g' in row:
            return 'yeongcheol'

arr = [list(input().split()) for _ in range(15)]
print(f(arr))