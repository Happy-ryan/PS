N = int(input())
S = input()

def solution(N, S):

    al = {
        'A': ['***', '*.*', '***', '*.*', '*.*'],
        'B': ['***', '*.*', '***', '*.*', '***'],
        'C': ['***', '*..', '*..', '*..', '***'],
        'D': ['***', '*.*', '*.*', '*.*', '***'],
        'E': ['***', '*..', '***', '*..', '***'],
    }

    answer = [''] * 5

    for c in S:
        for idx, code in enumerate(al[c]):
            answer[idx] += code

    for row in answer:
        print(row)
        
        
solution(N, S)