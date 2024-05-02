-- 코드를 작성해주세요
-- 물고기의 종류 별 이름과 잡은 수
-- 잡은 수 기준 내림차순

with tmp as (
    select ID, I.FISH_TYPE, N.FISH_NAME
    from FISH_INFO I 
    inner join FISH_NAME_INFO N on I.FISH_TYPE = N.FISH_TYPE
)

select count(ID) as FISH_COUNT, FISH_NAME
from tmp
group by FISH_NAME
order by count(ID) desc;