n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(m)]

def solution(n, m, A, B):
    
    votes = [0] * n
    
    for b in B:
        for idx, a in enumerate(A):
            if b >= a:
                votes[idx] += 1
                break
    
    max_vote = max(votes)
    
    return votes.index(max_vote) + 1

print(solution(n, m, A, B))