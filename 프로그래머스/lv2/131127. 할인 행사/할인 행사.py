from collections import Counter
def solution(want, number, discount):
    answer = 0
    want_dic = Counter()
    for i in range(len(want)):
        want_dic[want[i]] += number[i]
    
    range_dic = Counter(discount[0 : 0 + 10])
    
    if range_dic == want_dic: # 첫날 회원가입했을 때 
        answer += 1
        
    for i in range(1, len(discount)):
        if i + 9 < len(discount):
            # 딕셔너리를 하루 지날 때마다 갱신시키면 시간초과 나옴
            # 슬라이딩윈도우와 유사한 아이디어 활용하기
            range_dic[discount[i - 1]] -= 1
            if range_dic[discount[i - 1]] == 0:
                range_dic.pop(discount[i - 1])
            range_dic[discount[i + 9]] += 1
            # 문제점 : 구성은 같은데 range_dic에서는 사라진 것이 0으로 남음.
            # 그래서 value == 0 제외 > for문 돌리면 size가 달라져서 에러 발생
            # 새로운 딕셔너리 형성
            if range_dic == want_dic:
                answer += 1
        
    return answer