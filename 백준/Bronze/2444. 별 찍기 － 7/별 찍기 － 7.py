N = int(input())
for x in range(N):
  print(" "*(N-1-x)+'*'*(2*x+1) )
for y in range(1,N):
  print(" " *(y)+"*"*(2*(N-y)-1))