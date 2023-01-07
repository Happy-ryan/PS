def Divisor(n):
    divisorList = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            divisorList.append((n//i, i))
            # if i != n // i:
            #     divisorList.append((n//i))
    divisorList.sort()
    return divisorList

def solution(brown, yellow):
    answer = []
    carpet = Divisor(yellow)
    for row in  Divisor(brown + yellow):
        if (row[0] - 2, row[1] - 2) in  carpet:
            answer = list(row)
            break
    return answer