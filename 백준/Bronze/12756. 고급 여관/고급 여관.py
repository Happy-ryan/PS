attack_a, life_a = map(int, input().split())
attack_b, life_b = map(int, input().split())

def solution(attack_a, life_a, attack_b, life_b):
    while life_a > 0 and life_b > 0:
        life_a -= attack_b
        life_a = max(life_a, 0)
        life_b -= attack_a
        life_b = max(life_b, 0)
        
    if life_a > 0:
        return 'PLAYER A'
    if life_b > 0:
        return 'PLAYER B'
    return 'DRAW'

print(solution(attack_a, life_a, attack_b, life_b))