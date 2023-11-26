n = int(input())
m = int(input())

current_channel = 100

if m != 0:
    breakdowns = list(map(int, input().split()))
else:
    breakdowns = []
    
buttons = set(list(range(10))) - set(breakdowns)

def listToInt(row: list[int]):
    ans = 0
    for digit in row:
        ans *= 10
        ans += digit
    return ans



def dfs(level, k):
    global min_btn_cnt
    if level == k:
        # num: 고장나지 않은 숫자 버튼을 눌렀을 때 이동한 채널
        # btn_cnt: 버튼 누른 횟수
        num = listToInt(visited.copy())
        btn_cnt = len(visited.copy())
        # abs(n - num): 숫자 이동 후 +/-로 조절
        # aba(100 - n): 숫자 이동 없이 100에서 +/-로 이동
        if min(abs(n - num) + btn_cnt, abs(current_channel - n)) < min_btn_cnt:
            min_btn_cnt = min(abs(n - num) + btn_cnt, abs(current_channel - n))
            # print(f"이동: {num}, 버튼: {min_btn_cnt}")
            # print("|==|"*30)
        return
    
    for btn in buttons:
        visited.append(btn)
        dfs(level + 1, k)
        visited.pop()
        
ans = []
k = len(str(n))
for x in range(1, 7):
    visited = []
    min_btn_cnt = int(1e8)
    dfs(0, x)
    
    if min_btn_cnt == int(1e8):
        ans.append(abs(current_channel - n))
    else:
        ans.append(min_btn_cnt)
        
print(min(ans))