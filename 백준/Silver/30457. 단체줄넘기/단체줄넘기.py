n = int(input())
arr = list(map(int, input().split()))

arr.sort()

p1, p2 = [], []

for idx, a in enumerate(arr):
    if a not in p1:
        p1.append(a)
        
p2 = arr
for p in p1:
    idx = p2.index(p)
    p2.pop(idx)
p2 = set(p2)

print(len(p1) + len(p2))