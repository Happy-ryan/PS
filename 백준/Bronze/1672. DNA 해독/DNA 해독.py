decoder = { 'AA': 'A',
            'AG': 'C',
            'AC': 'A',
            'AT': 'G',
            'GA': 'C',
            'GG': 'G',
            'GC': 'T',
            'GT': 'A',
            'CA': 'A',
            'CG': 'T',
            'CC': 'C',
            'CT': 'G',
            'TA': 'G',
            'TG': 'A',
            'TC': 'G',
            'TT': 'T'}

n = int(input())
s = list(input())
while len(s) > 1:
    last = s[-2] + s[-1]
    s.pop()
    s.pop()
    s.append(decoder[last])

print(*s)