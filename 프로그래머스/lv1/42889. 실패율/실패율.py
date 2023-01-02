def solution(N, stages):
    answer = []
    numInstage = [0] * (N + 2)
    for num in stages:
        numInstage[num] += 1
    print(numInstage)
    
    fail_per = [0] * (N + 1)
    for i, x in enumerate(numInstage[1:-1]):
        # print(i + 1, x,  sum(numInstage[i+1:]))
        if x == 0:
            fail_per[i + 1] = 0
        else:
            fail_per[i+1] = x / sum(numInstage[i+1:])
    for i, per in enumerate(fail_per[1:]):
        answer.append((-per, i+1))
    answer.sort()
    print(answer)
    
    res = []
    for per, i in answer:
        res.append(i)
        
    return res