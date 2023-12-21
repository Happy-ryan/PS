# https://www.acmicpc.net/problem/2841
from collections import defaultdict
n, p = map(int, input().split())
# 각 줄은 독립적!
guitar_strings_melody = dict()
for _ in range(n):
    string_number, plat_number = map(int, input().split())
    if string_number not in guitar_strings_melody.keys():
        guitar_strings_melody[string_number] = []
        guitar_strings_melody[string_number].append(plat_number)
    else:
        guitar_strings_melody[string_number].append(plat_number)
    

def count_finger_number(plats: list[int]):
    # stack[-1]이 가장 큰수가 되도록 했음. > 마지막에 위치한 것만 소리남!
    stack = []
    cnt = 0
    for plat in plats:
        if len(stack) == 0:
            stack.append(plat)
            cnt += 1
        else:
            # 새로운 plat이 더 크면 넣기!
            if stack[-1] < plat:
                stack.append(plat)
                cnt += 1
            # 새로운 plat이 더 작은 경우.
            else:
                # 새로운 plat이 제일 큰 숫자가 될 때까지 pop
                while True:
                    # 전부 빼면 다시 넣기
                    if len(stack) == 0:
                        stack.append(plat)
                        cnt+=1
                        break
                    # 빼다가 새로운 plat이랑 마지막 plat이 같으면
                    # 기존의 plat이므로 넣지 않기
                    if stack[-1] == plat:
                        break
                    # 새로운 plat이 더 크면 넣기
                    if stack[-1] < plat:
                        stack.append(plat)
                        cnt += 1
                        break
                    stack.pop()
                    cnt += 1
    return cnt

ans = 0
for key in guitar_strings_melody.keys():
    ans += count_finger_number(guitar_strings_melody[key])
print(ans)