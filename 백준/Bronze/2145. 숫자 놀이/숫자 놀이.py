def sum(x): #자리수를 더한 값을 구하는 함수
    arr = list((str(x)))
    result = 0
    for x in arr:
        result += int(x)
    return result

while True:
    n = int(input())
    k = n
    if k == 0:
        break
    else:
        while True:
            num = sum(k)
            if num < 10:
                print(num)
                break
            else:
                k = num