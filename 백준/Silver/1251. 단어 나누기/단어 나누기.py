s = list(input())

# 리스트 안의 원소가 문자일 때 다 더해주는 함수
def f(list):
    str =""
    for x in list:
        str += x

    return str
# 슬라이싱으로 문자열 2등분
result = []
idx = 0
for i in range(len(s)-2):
    for j in range(i+1,len(s)-1):
        part1 = s[:i+1][::-1]
        part2 = s[i+1:j+1][::-1]
        part3 = s[j+1:][::-1]
        final_s = part1+part2+part3
        # print(part1,part2,part3)
        # print("마지막",final_s)
        result.append(f(final_s))

result.sort()
print(result[0])