-- 코드를 입력하세요
# 09:00 ~ 19:59 각 시간대별로
# 입양이 몇 건 
# 시간순으로 정렬

select hour(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by hour(DATETIME)
order by hour(DATETIME);

select *
from ANIMAL_OUTS;

select  year(DATETIME) as year,
        month(DATETIME) as month,
        day(DATETIME) as day,
        hour(DATETIME) as hour,
        minute(DATETIME) as minute,
        second(DATETIME) as second
from ANIMAL_OUTS;

select *
from ANIMAL_OUTS;

select hour(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by HOUR
order by HOUR;