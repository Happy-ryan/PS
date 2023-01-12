from functools import cmp_to_key

def solution(strings, n):

    def compare(x, y):
        if x[n] != y[n]:
            if x[n] > y[n]: 
                return -1
            else: 
                return 1
        else:
            if x > y:
                return -1
            else:
                return 1

    strings.sort(key = cmp_to_key(compare), reverse = True)
    return strings
