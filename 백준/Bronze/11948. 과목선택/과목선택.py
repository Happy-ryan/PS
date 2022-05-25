A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
science = [A,B,C,D]
science = sorted(science)
society = [E,F]
print(sum(science[1:])+max(society))