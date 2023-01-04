def window(arr, k):
    budget_sum = []
    res = sum(arr[0: k])
    budget_sum.append(res)
    for i in range(1, len(arr) - k + 1):
        res -= arr[i - 1]
        res += arr[i + k - 1]
        budget_sum.append(res)
    
    return budget_sum

def solution(d, budget):
    answer = 0
    d.sort()
    for k in range(1, len(d) + 1):
        for money in window(d, k):
            if budget >= money:
                answer = max(answer, k)
    return answer