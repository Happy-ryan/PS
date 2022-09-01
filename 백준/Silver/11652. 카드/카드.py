N = int(input())
arr_list = sorted([int(input()) for row in range(N)])
arr_set = set(arr_list)

num_dict ={}
for x in arr_set:
    num_dict[x] = 0

for k in arr_list:
    num_dict[k] += 1

# print(num_dict)
# items() : (key,value) 튜플 생성 
# values() : value 리스트 생성
inf = 10e18
ans = int(inf)
max_value = max(num_dict.values())
for k,v in num_dict.items():
    if max_value == v:
        ans = min(ans,k)
print(ans)