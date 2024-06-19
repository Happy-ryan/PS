n = int(input())
votes = list(map(int, input().split()))

def solution(n, votes):
    a, r, i = 0, 0, 0
    
    a += votes.count(1)
    r += votes.count(-1)
    i += votes.count(0)
    
    if i >= n / 2:
        return 'INVALID'

    if r >= a:
        return 'REJECTED'
    return 'APPROVED'

print(solution(n, votes))