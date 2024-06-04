n = int(input())
m = int(input())
targets = list(map(int, input().split()))
rounds = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, targets, rounds):
    friends = [0] * (n + 1)
    for idx, round in enumerate(rounds):
        wrong = 0
        for friend_number, expect_target in enumerate(round):
            if targets[idx] == expect_target:
                friends[friend_number + 1] += 1
            else:
                wrong += 1
        friends[targets[idx]] += wrong
    
    for x in friends[1:]:
        print(x)
        
solution(n, m, targets, rounds)