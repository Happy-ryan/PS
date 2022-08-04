arr = input()

def happy_cnt(arr):
    sum = 0
    happy_arr_blank_is = arr.split(":-)")
    sum = len(happy_arr_blank_is)-1
    return sum

def unhappy_cnt(arr):
    sum = 0
    unhappy_arr_blank_is = arr.split(":-(")
    sum = len(unhappy_arr_blank_is)-1
    return sum

def final_check(arr):
    if (happy_cnt(arr) == 0) and (unhappy_cnt(arr)==0):
        return 'none' 
    elif happy_cnt(arr) > unhappy_cnt(arr):
        return 'happy'
    elif happy_cnt(arr) < unhappy_cnt(arr):
        return 'sad'
    else: 
        return "unsure"

print(final_check(arr))