# https://www.acmicpc.net/problem/2840

# S의 의미: 1바퀴 회전시켰을 때 몇 칸을 움직이냐?
# HONITAVR, 현재H  -> 시계방향회전
# 1바퀴 회전 3번이동: H -> A

# 예시 [1, A], [2, B], [3, C]
# 화살표는 배열의 항상 첫번째를 가르킨다고 가정한다!
# 초기 123(반시계상태로 적혀있음) 따라서 회전하면 맨앞에 있는 것이 뒤로 가게 된다.
# 1바퀴 회전 ->S - 1번이동 - 가르키는 곳 (최종) 231
# 1바퀴 회전 ->S - 2번이동 - 가르키는 곳 (최종)231 -> 312 -> (최종) 123 
# 1바퀴 회전 ->S - 3번이동 - 가르키는 곳 최종)123 -> 231 -> 312 -> (최종) 123
# 2-A / 1 - B / 1 - C > 같은 번호판에 다른 문자 존재 > 해당하는 행운판이 없는 것!!
# ?는 언제 나올까? 예제2번 분석하면 같은 번호판에 같은 문자들이 몰려서 비어있는 칸이 존재함

n, k = map(int, input().split())
memos = [input().split() for _ in range(k)]

def rotate(fortune_wheel: list[int], S: int):
    S %= n
    for _ in range(S):
        fortune_wheel = [fortune_wheel[-1]] + fortune_wheel[:-1]
    return fortune_wheel

fortune_wheel = list(range(1, n + 1))
# [] 한 이유: 다른 mark가 들어가면 !
mark_memo = [ [] for _ in range(n + 1)]
# 마지막 mark가 어디에 있는지 알기위해서 초기화
final_mark_index = 1
for S, mark in memos:
    fortune_wheel = rotate(fortune_wheel, int(S))
    mark_memo[int(fortune_wheel[0])].append(mark)
    final_mark_index = int(fortune_wheel[0])
    
#   (요기 방향으로 읽기)  ->|마지막 mark 기준으로| ->(여기방향으로 먼저 읽고)
res = ''
for _ in range(n + 1):
    # 맨 앞은 인덱스때문에 만들어놓은거니까 고려안함
    # 맨 앞까지 왔다는건 이제 <- 이 방향 읽어야하므로 final_mark_index 마지막으로 초기화
    if final_mark_index == n + 1:
        final_mark_index = 1
        continue
    row = set(mark_memo[final_mark_index])
    if len(row) == 0:
        res += '?'
    elif len(row) == 1:
        mark = mark_memo[final_mark_index][0]
        res += mark
    else:
        res = "!"
        break
    final_mark_index += 1

def is_duplicate_char(res):
    char_count = {}
    for char in res:
        if char == '?':
            continue
        if char in char_count:
            return True  
        else:
            char_count[char] = 1
    return False


if is_duplicate_char(res):
    print("!")
else:
    print(res)