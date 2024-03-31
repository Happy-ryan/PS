# 3 ~ n + 2 입장번호 제공
# 한 학생에게 출석코드를 보내게 되면,
# 하댕 학생은 본인의 입장 *번호의 배수*인 학생들에게 출석코드를 보내어 해당 강의 출석하게끔!

# k명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.
# 학생의 수 n, 졸고 있는 학생의 수 k, 지환이가 출석 코드를 보낼 학생의 수 q, 주어질 구간의 수 m
n, k, q, m = map(int, input().split())
sleep_students = list(map(int, input().split()))
code_students = list(map(int, input().split()))
qs = [list(map(int, input().split())) for _ in range(m)]


def solution(n, k, q, m, sleep_students, code_students, qs):
    check = [1 for _ in range(n + 3)]

    sleep_students = set(sleep_students)
    # 5000(q) * ( 5000(k) +  5000(n) * 5000(k) )
    # 5000 * 5000 * (1 + 5000) > 5000^3: 시간초과
    # 5000 * (1 + 5000 * 1) > 5000^2 >25 10^6 = 2.5  * 10^7
    for code in code_students:
        # 자는 애는 전파 불가
        if code in sleep_students:
            continue
        for x in range(code, n + 3, code):
            # code는 전파되는데 자는 애는 받으면 안된다.
            if x in sleep_students:
                continue
            check[x] = 0
    # qs: 50000 * 5000 (n + 3) > 25 * 10^7 > 2.5 * 10^8
    # 특정 구간의 1의 개수 찾기
    # 1 2 3 4 5 6 7 8 9 10
    # 0 1 0 0 1 1 0 0 1 0
    # 누적합의 정의는 처음부터 내 위치까지의 1의 개수
    # '0' 0 1 1 1 2 3 3 3 4 4
    # 예를 들어 5 ~ 6 번 구간에 1이 몇 개의 1이 존재하냐?
    # f(6번) = 1번 위치에서의 1의 개수 + ... + 6번 위치에서의 1의개수
    # f(5번) = 1번 위치에서의 1의 개수 + .. + 5번 위치에서의 1의 개수
    # 5 ~ 6번구간 1의 개수 = f(6번) - f(4번) = 6번 위치에서의 1의 개수 + 5번 위치에서의 1의 개수
    check = check[3:] 
    psum = [0] * (n + 1)
    # psum[1] = psum[0] + check[0]
    for i in range(n):
        psum[i + 1] = check[i] + psum[i]

    for q in qs:
        s, e = q
        print(psum[e - 2] - psum[s - 3])


solution(n, k, q, m, sleep_students, code_students, qs)