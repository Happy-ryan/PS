N = int(input())
A,B = map(int,input().split())
possible_chicken = (A//2) + B
print( possible_chicken if N>=possible_chicken else N) 