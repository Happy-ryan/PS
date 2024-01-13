from collections import Counter
n, game = input().split()
n = int(n)
people = Counter([input() for _ in range(n)])
game_need = {'Y' : 1, 'F' : 2, 'O' : 3}
print(len(people.keys()) // game_need[game])