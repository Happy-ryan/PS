# https://www.acmicpc.net/problem/17305
N, w = map(int, input().split())
candies = [tuple(map(int, input().split())) for _ in range(N)]
# 같은 당도라면 무게가 낮은게 좋지 않을까?
candies.sort(key=lambda x: (-x[1], x[0]))

three_weight_candies = []
five_weight_candies = []

for row in candies:
    if row[0] == 3:
        three_weight_candies.append(row)
    else:
        five_weight_candies.append(row)
        
def choose_only(candy_list, w):
    ans = 0
    res = []
    for weight, sugar in candy_list:
        if 0 <= w - weight:
            w -= weight
            ans += sugar
            res.append(sugar)
            # print(f"weight: {weight}, sugar: {sugar}")
    remain = w
    return remain, ans, res

# 무게3으로 최대한 넣는 것을 고려했으므로 이제는 3은 고려할 필요가 없다!!!
remain, ans, res = choose_only(three_weight_candies, w)
# 이제 5만 고려하면 된다.
idx = 0
max_ans = ans
k = len(res)
for _ in range(k + 1):
    while remain >= 5 and idx < len(five_weight_candies):
        remain -= 5
        ans += five_weight_candies[idx][1]
        max_ans = max(max_ans, ans)
        idx += 1
    if len(res) != 0:
        remove_sugar = res.pop()
        ans -= remove_sugar
        remain += 3
    
print(max_ans)