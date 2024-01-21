# https://www.acmicpc.net/problem/2817

X = int(input())
N = int(input())
infos = [input().split() for _ in range(N)]
# 점수집합 
res = []
# 5% 이상 득표 staff 목록
staff_five_precent = []
# N = 0 이거나 참가자 전원이 5퍼센트 미만을 받은 경우 <- 틀린이유 후보
is_nothing = True
for staff, cnt in infos:
    cnt = int(cnt)
    #  전체 대회 참가자(X)의 5% 미만의 득표 제거 
    # //로 나눠서 틀린건가?? 왜냐하면 소수점이 사라지면서 cnt를 잘못 판단할 수 있을 것 같음.
    # 혹시 투표를 부정하게 받으면 제거? <- 틀린이유 후보
    if cnt > X or cnt < (X * 5) / 100:
        continue
    staff_five_precent.append(staff)
    for i in range(1, 15):
        res.append((cnt / i ,staff))
    is_nothing = False

# 점수로 내림차순정렬
# 점수집합에 있는 실수들은 항상 서로 다르도록 투표결과가 나온다고 한다.
res.sort(key=lambda x: -x[0])
# 출력할 때 사전순
staff_five_precent.sort()
# 득표수 기록 배열
ans = [0 for _ in range(26)]
# 14개의 칩을 나눠주므로 14개까지만 확인
for _, staff in res[:14]:
    ans[ord(staff) - 65] += 1

# 5퍼센트 이상이면 0도 출력해야하는거 아닐까? <- 틀린이유 후보
# 무슨 말이냐면,,5퍼센트 이상 득표했는데 상위 14명 안에 못 들을 수 있는 경우를 말한다.
# 따라서 res에 존재하는 staff들을 알 필요가 있다.
if is_nothing:
    print(0)
else:
    for staff in staff_five_precent:
        print(f"{staff} {ans[ord(staff) - 65]}")