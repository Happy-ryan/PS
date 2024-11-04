word = input()

def solution(word):
    res = []
    part1, part2, part3 = '', '', ''
    for mid1 in range(1, len(word) -1):
        for mid2 in range(1, len(word)):
            if mid1 <  mid2:
                part1 += word[0: mid1]
                part2 += word[mid1: mid2]
                part3 += word[mid2:]
                # print(f"part1: {part1}, part2: {part2}, part3: {part3}")
                res.append(part1[::-1] + part2[::-1] + part3[::-1])
                part1 = ''
                part2 = ''
                part3 = ''
    res.sort()
    
    return res[0]

print(solution(word))