def dfs(lev, numbers, d, used, visited, final): # 순열, 중복사용 불가
    if lev == d:
        a = int(''.join(visited.copy()))
        final.add(a)
        return
    for i in range(len(numbers)):
        if used[i] == 0:
            used[i] = 1
            visited.append(numbers[i])
            dfs(lev + 1, numbers, d, used, visited, final)
            used[i] = 0
            visited.pop()
    return final

def isPrime(n):
    primes = []
    a = [False, False] + [True] * (n - 1)
    
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(i*i, n + 1, i):
                a[j] = False
    
    return primes

def solution(numbers):
    answer = 0
    used = [0] * len(numbers)
    visited = []
    final = set()
    for i in range(1, len(numbers) + 1):
        dfs(0, numbers, i, used, visited, final)
    for x in isPrime(max(final)):
        if x in final:
            answer += 1
    return answer