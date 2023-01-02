res = set()
def f(s): # 2개씩
    s = s.lower()
    two_arr = []
    for i in range(len(s) - 1):
        row = s[i:i+2]
        if row.isalpha():
            res.add(row)
            two_arr.append(row)
    return two_arr

from collections import Counter

def solution(str1, str2):
    answer = 0
    p, q = 0, 0 # 교집합의 원소의수 , 합집합의 원소의 수
    f(str1)
    f(str2)
    print(res)
    str1_dict = Counter(f(str1))
    str2_dict = Counter(f(str2))
    print(str1_dict)
    print(str2_dict)
    for row in res:
        p += min(str1_dict[row], str2_dict[row])
        q += max(str1_dict[row], str2_dict[row])
    if len(str1_dict.keys()) == 0 and len(str2_dict.keys()) == 0:
        return 1 * 65536
    else:
        if len(str2_dict.keys()) == 0:
            return 1 * 65536
        else:
            print(p, q)
            answer = int(65536 * p / q)
            return int(answer)