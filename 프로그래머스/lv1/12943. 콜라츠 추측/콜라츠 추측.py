def solution(num):
    play = 0
    while play <= 500:
        if num == 1:
            break
        else:
            play += 1
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
    if play > 500:
        return -1
    else:
        return play
    return answer