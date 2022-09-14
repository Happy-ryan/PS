import sys

input = sys.stdin.readline

N = int(input())
arr = input()
A = 0
B = 0
for s in arr:
  if s == 'A':
    A += 1
  elif s == 'B':
    B += 1

if A > B:
  print('A')
elif A < B:
  print('B')
else:
  print('Tie')