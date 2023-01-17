def solution(s):
    answer = ''
    s = list(s.lower()) # 전부 소문자로 바꾸기
    # word_start가 단어의 시작
    # 공백 + 단어시작 > 단어시작 word_start를 지속적으로 갱신하여 
    # word_start와의 거리 차이를 통해서 인덱스 파악하기
    word_start = 0
    for i, x in enumerate(s):
        if (i - word_start) % 2 == 0:
            s[i] = s[i].upper() 
        # index를 i, i + 1 사용할 때는 len(s) - 1까지 사용하나
        # enumerate때문에 불가하므로 조건문에 추가
        if i + 1 < len(s) and x == ' ' and s[i + 1] != ' ': 
            word_start = i + 1
    return ''.join(s)