x = input()

def solution(x):
    s = list(map(int, str(x)))
    n = len(s)
    if n < 2:
        return "NON ALPSOO"  # 자릿수 부족

    # 평지 여부
    for i in range(n-1):
        if s[i] == s[i+1]:
            return "NON ALPSOO"

    # 처음이 오르막인지 확인
    first_diff = s[1] - s[0]
    if first_diff <= 0:
        return "NON ALPSOO"

    # 마지막이 내리막인지 확인할 거라서, 마지막 차를 추적
    prev_diff = first_diff

    for i in range(1, n-1):
        diff = s[i+1] - s[i]
        # 평지는 이미 체크했지만 diff == 0 은 안전하게 NON
        if diff == 0:
            return "NON ALPSOO"

        # 방향이 유지되고 있으면 (부호 동일) 
        if (prev_diff > 0 and diff > 0) or (prev_diff < 0 and diff < 0):
            # 기울기 크기가 같아야 함
            if diff != prev_diff:
                return "NON ALPSOO"
            # direction이 바뀐 적 없고 계속 + 혹은 계속 −이면 기울기 검사
        # 방향이 바뀌면 그냥 넘어가고 새로운 방향부터 검사
        prev_diff = diff

    # 마지막 diff (prev_diff) 이 내리막(음수)여야 함
    if prev_diff >= 0:
        return "NON ALPSOO"

    return "ALPSOO"

# 입력/출력 부분
print(solution(x))
