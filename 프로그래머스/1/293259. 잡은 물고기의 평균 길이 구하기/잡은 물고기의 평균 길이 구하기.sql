-- 코드를 작성해주세요
# select round(avg(ifnull(LENGTH, 10)),2) as AVERAGE_LENGTH
# from FISH_INFO;

# 10cm의 물고기의 length는 null로 표현 -> 10cm로 취급
select round(avg(ifnull(length, 10)), 2) as AVERAGE_LENGTH
from FISH_INFO;