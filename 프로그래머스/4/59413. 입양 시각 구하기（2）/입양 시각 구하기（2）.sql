-- 코드를 입력하세요
# 몇 시에 입양이 가장 활발하게 일어나는지?
# 0 ~ 23시 / 각 시간대별로 입양이 발생한 건수
# 시간대로 정렬

with temp as(
select 0 as HOUR
union
select 1 as HOUR
union
select 2 as HOUR
union
select 3 as HOUR
union
select 4 as HOUR
union
select 5 as HOUR
union
select 6 as HOUR
union
select 7 as HOUR
union
select 8 as HOUR
union
select 9 as HOUR
union
select 10 as HOUR
union
select 11 as HOUR
union
select 12 as HOUR
union
select 13 as HOUR
union
select 14 as HOUR
union
select 15 as HOUR
union
select 16 as HOUR
union
select 17 as HOUR
union
select 18 as HOUR
union
select 19 as HOUR
union
select 20 as HOUR
union
select 21 as HOUR
union
select 22 as HOUR
union
select 23 as HOUR
), temp2 as (
    select hour(DATETIME) as HOUR, count(*) as COUNT
    from ANIMAL_OUTS
    group by HOUR
    order by HOUR
)

select temp.HOUR, ifnull(temp2.COUNT, 0) as COUNT
from temp
left join temp2 on temp.HOUR = temp2.HOUR;