import math
def f(n): # 약수의 개수
    divisorList = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisorList.append(i)
            if i != n//i:
                divisorList.append(n//i)
    divisorList.sort()
    
    return divisorList

def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        if len(f(num)) > limit:
            answer += power
        else:
            answer += len(f(num))
    return answer