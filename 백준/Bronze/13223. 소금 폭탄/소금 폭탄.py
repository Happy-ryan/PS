# 시간/날 문제는 단위수로 환산하여 문제 풀기 
time1 = input()
time2 = input()

def solution(time1, time2):
    h1, m1, s1 = map(int, time1.split(':'))
    h2, m2, s2 = map(int, time2.split(':'))
    
    def change_time(h, m, s):
        return h * 3600 + m * 60 + s
    
    def restore_time(total):
        # total 은 초를 의미함!
        h = total // 3600
        m = (total % 3600) // 60
        s = (total % 3600) % 60
        return f"{h:02}:{m:02}:{s:02}"
    
    total1 = change_time(h1, m1, s1)
    total2 = change_time(h2, m2, s2)
    
    if total1 < total2:
        return restore_time(total2 - total1)
    
    if total1 >= total2:
        return restore_time(total2 + change_time(24, 0, 0) - total1)
    
print(solution(time1, time2))