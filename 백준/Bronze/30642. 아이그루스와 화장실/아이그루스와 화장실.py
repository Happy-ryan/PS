n = int(input())
ch = input()
spot = int(input())

def solution(n, ch, spot):
    if ch == 'annyong':
        if spot % 2 == 0:
            return max(min(abs(spot + 1), abs(spot - 1), n), 1)
        else:
            return spot
    else:
        if spot % 2 == 0:
            return spot
        else:
            return max(min(abs(spot + 1), abs(spot - 1), n), 2)

print(solution(n, ch, spot))