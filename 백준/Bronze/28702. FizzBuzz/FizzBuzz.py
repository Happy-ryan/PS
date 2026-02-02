def solution(arr):
    
    # 3개 중 마지막 숫자의 인덱스 찾기
    idx = 0
    for i, a in enumerate(arr):
        if a.isdigit():
            idx = i
            
    number = int(arr[idx]) + (3 - idx)
    
    if number % 3 == 0:
        if number % 5 == 0:
            return 'FizzBuzz'
        else:
            return 'Fizz'
    else:
        if number % 5 == 0:
            return 'Buzz'
        else:
            return number

arr = [input() for _ in range(3)]
print(solution(arr))