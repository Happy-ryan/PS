-- 코드를 입력하세요
# SELECT DATETIME
# FROM ANIMAL_INS
# # 최근에 들어온 것이므로 내림차순
# ORDER BY DATETIME DESC
# LIMIT 1;

select DATETIME
from ANIMAL_INS
where DATETIME = (
    select max(DATETIME) 
    from ANIMAL_INS);
