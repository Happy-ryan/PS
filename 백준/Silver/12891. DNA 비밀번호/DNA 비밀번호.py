# https://www.acmicpc.net/problem/12891
# p, s 1,000,000
s, p = map(int, input().split())
dna = input()
standard_list = list(map(int, input().split()))

def count_chracter(part_dna: str):
    dic = {"A": 0, "C": 0, "G": 0, "T": 0}
    # 시간복잡도 len(part_dna) 
    dic["A"] = part_dna.count("A")
    dic["C"] = part_dna.count("C")
    dic["G"] = part_dna.count("G")
    dic["T"] = part_dna.count("T")
    return dic

def check(standard_list: list[int], target_dict: dict):
    check_list = ["A", "C", "G", "T"]
    for idx, check in enumerate(check_list):
        if standard_list[idx] > target_dict[check]:
            return 0
    return 1

# 시간복잡도 슬라이싱 > n^2 > 시간초과
# 슬라이딩 윈도우..?
# 기존의 l과 새로운 r을 집중해야한다.
l = 0
r = l + p - 1
target_dict = count_chracter(dna[l : r + 1])

ans = check(standard_list, target_dict)

while r < s - 1:
    if dna[l] == "A":
        target_dict["A"] -= 1
    elif dna[l] == "C":
        target_dict["C"] -= 1
    elif dna[l] == "G":
        target_dict["G"] -= 1
    else:
        target_dict["T"] -= 1
    l += 1
    r += 1
    if dna[r] == "A":
        target_dict["A"] += 1
    elif dna[r] == "C":
        target_dict["C"] += 1
    elif dna[r] == "G":
        target_dict["G"] += 1
    else:
        target_dict["T"] += 1
    
    ans += check(standard_list, target_dict)
    
print(ans)