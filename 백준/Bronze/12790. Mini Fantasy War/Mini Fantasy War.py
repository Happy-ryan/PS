t = int(input())
for _ in range(t):
    hp, mp, attack, defence, dhp, dmp, dattack, ddefence = map(int, input().split())
    
    hp = max(1, hp + dhp)
    mp = max(1, mp + dmp)
    attack = max(0, attack + dattack)
    defence += ddefence
    print(1 * hp + 5 * mp + 2 * attack + 2 * defence)