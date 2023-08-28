s1 = input()
s2 = input()
ans = ""
for idx, x in enumerate(s1):
    # 공백 유지
    if x == ' ':
        ans += ' '
    # 공백 제외 평문의 아스키코드
    else:
        orgin = ord(s1[idx])
        # 암호화 키의 알파벳 순서 -> 암호화 키 안에서 돌기 때문에 모듈러 연산 도입! -> 나머지
        p = idx % len(s2)
        key = ord(s2[p]) - ord('a') + 1
        # 암호화 아스키 코드
        en = orgin - key
        # en이 a보다 작아질 경우 z로 되돌아가 값 출력
        if 97 <= en and en <= 122:
            ans += chr(en)
        else:
            en += 26
            ans += chr(en)
print(ans)