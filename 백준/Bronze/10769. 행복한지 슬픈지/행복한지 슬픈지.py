arr = input()
# brr = arr.split(":-)")
# crr = arr.split(":-(")
# print(":-)",brr)
# print("brr의 길이:",len(brr))
# print(":-(",crr)
# print("crr의 길이:",len(crr))

def happy_cnt(arr):
    sum = 0
    happy_arr_blank_is = arr.split(":-)")
    happy_arr_blank_not = [ x for x in happy_arr_blank_is if x] # list comprehesion & 조건문 사용하여 공백제거
    sum = len(happy_arr_blank_is)-1
    return sum

def unhappy_cnt(arr):
    sum = 0
    unhappy_arr_blank_is = arr.split(":-(")
    unhappy_arr_blank_not = [ x for x in unhappy_arr_blank_is if x] # list comprehesion & 조건문 사용하여 공백제거
    sum = len(unhappy_arr_blank_is)-1
    return sum

# print(happy_cnt(arr))
# print(unhappy_cnt(arr))
if (happy_cnt(arr) == 0) and (unhappy_cnt(arr)==0):
    print('none') 
elif happy_cnt(arr) > unhappy_cnt(arr):
    print('happy')
elif happy_cnt(arr) < unhappy_cnt(arr):
    print('sad')
else: print("unsure")