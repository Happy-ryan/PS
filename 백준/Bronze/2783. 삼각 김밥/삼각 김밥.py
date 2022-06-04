X,Y = map(int, input().split())
N = int(input())
arr = [input().split() for _ in range(N)]
arr = [[int(a),int(b)] for a,b in arr]
gs = (1000*X)/Y

result = set()
result.add(gs)
for i in range(len(arr)):
  price = ((1000*arr[i][0])/(arr[i][1]))
  result.add(price)
# print(result)
min_price = min(result)
min_price = round(min_price,2)
print(min_price)