T = int(input())

for tc in range(1, T + 1):
    B = int(input())
    s = input()
    
    result = []
    for i in range(0, 8 * B, 8):
        byte = s[i:i+8]
        binary = byte.replace('I', '1').replace('O', '0')
        ascii_code = int(binary, 2)
        result.append(chr(ascii_code))
    
    print(f"Case #{tc}: {''.join(result)}")
