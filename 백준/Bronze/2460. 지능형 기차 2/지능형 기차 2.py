arr = [ input().split() for _ in range(10)]
arr = [[int(a),int(b)] for a,b in arr]
# print(arr)
cnt = 0
people_num = set()
for i in range(10):
    cnt -= arr[i][0]
    cnt += arr[i][1]
    people_num.add(cnt)
print(max(people_num))