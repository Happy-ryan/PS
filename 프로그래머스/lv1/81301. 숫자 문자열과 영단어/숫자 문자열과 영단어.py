def f(num):
    if num == 'zero':
        return '0'
    elif num == 'one':
        return '1'
    elif num == 'two':
        return '2'
    elif num == 'three':
        return '3'
    elif num == 'four':
        return '4'
    elif num == 'five':
        return '5'
    elif num == 'six':
        return '6'
    elif num == 'seven':
        return '7'
    elif num == 'eight':
        return '8'
    elif num == 'nine':
        return '9'

def solution(arr):
    answer = ''
    s, e = 0, 0
    while s < len(arr) and e < len(arr):
        if arr[s].isdigit():
            answer += arr[s]
            s += 1
        else:
            if arr[s] == 'z':
                e = s + 4
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 'o':
                e = s + 3
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 't' and arr[s+1] == 'w':
                e = s + 3
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 't' and arr[s+1] == 'h':
                e = s + 5
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 'f' and arr[s+1] == 'o':
                e = s + 4
                answer += f(arr[s : e])
                s = e
            elif arr[s] == 'f' and arr[s+1] == 'i':
                e = s + 4
                answer += f(arr[s : e])
                s = e
            elif arr[s] == 's' and arr[s+1] == 'i':
                e = s + 3
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 's' and arr[s + 1] == 'e':
                e = s + 5
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 'e':
                e = s + 5
                answer += f(arr[s : e])
                s = e 
            elif arr[s] == 'n':
                e = s + 4
                answer += f(arr[s : e])
                s = e 
    return int(answer)
