scores = [13, 7, 5, 3, 3, 2]
carr = list(map(int, input().split()))
earr = list(map(int, input().split()))

c, e = 0, 0
for i in range(6):
    c += carr[i] * scores[i]
    e += earr[i] * scores[i]
    
e += 1.5
if c > e:
    print('cocjr0208')
else:
    print('ekwoo')