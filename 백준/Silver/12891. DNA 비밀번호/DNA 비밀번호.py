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
    for idx, check in enumerate("ACGT"):
        if standard_list[idx] > target_dict[check]:
            return 0
    return 1

l = 0
r = l + p - 1
target_dict = count_chracter(dna[l : r + 1])

ans = check(standard_list, target_dict)


while r < s - 1:
    target_dict[dna[l]] -= 1
    l += 1
    r += 1
    target_dict[dna[r]] += 1
    
    ans += check(standard_list, target_dict)
    
print(ans)