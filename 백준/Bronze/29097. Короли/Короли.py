n, m, k, a, b, c = map(int, input().split())

powers = {'Joffrey': a * n,
          'Robb': b * m,
          'Stannis' : c * k} # J, R, S

max_p = max(powers.values())

for person, power  in powers.items():
    if max_p == power:
        print(person, end= ' ')