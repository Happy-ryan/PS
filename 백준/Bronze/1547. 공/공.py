M = int(input())
arr =[ input().split() for _ in range(M)]
arr = [[int(a) ,int(b)] for a,b in arr]
#print(arr)
cups = [1,0,0]
for row in arr:
    cups[row[0]-1],cups[row[1]-1] = cups[row[1]-1],cups[row[0]-1] 

print(cups.index(1)+1)