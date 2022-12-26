def solution(absolutes, signs):
    sum = 0
    for i, x in enumerate(signs):
        if x == True:
            sum += absolutes[i]
        else:
            sum -= absolutes[i]
    return sum