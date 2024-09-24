sL, sR = input().split()
ans = input()

def solution(sL, sR, ans):
    # (x, y, 자음/모음판단)
    keyboard = {
        'q': (0, 0, 1),
        'w': (0, 1, 1),
        'e': (0, 2, 1),
        'r': (0, 3, 1),
        't': (0, 4, 1),
        'y': (0, 5, 0),
        'u': (0, 6, 0),
        'i': (0, 7, 0),
        'o': (0, 8, 0),
        'p': (0, 9, 0),
        'a': (1, 0, 1),
        's': (1, 1, 1),
        'd': (1, 2, 1),
        'f': (1, 3, 1),
        'g': (1, 4, 1),
        'h': (1, 5, 0),
        'j': (1, 6, 0),
        'k': (1, 7, 0),
        'l': (1, 8, 0),
        'z': (2, 0, 1),
        'x': (2, 1, 1),
        'c': (2, 2, 1),
        'v': (2, 3, 1),
        'b': (2, 4, 0),
        'n': (2, 5, 0),
        'm': (2, 6, 0)
    }
    
    typing_time = len(ans)
    moving_time = 0
    
    def cal(a1, a2):
        return abs(keyboard[a1][0] - keyboard[a2][0]) + abs(keyboard[a1][1] - keyboard[a2][1])
    
    for x in ans:
        # 한글자음
        if keyboard[x][2] == 1:
            moving_time += cal(sL, x)
            sL = x
        else:
            moving_time += cal(sR, x)
            sR = x
            
    return typing_time + moving_time

print(solution(sL, sR, ans))