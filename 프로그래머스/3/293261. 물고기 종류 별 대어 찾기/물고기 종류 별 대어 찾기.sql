-- 코드를 작성해주세요
-- 종류별 가장 큰 물고기를 찾아라
-- ID기준 오름차순

with tmp as (
select  I.ID, I.FISH_TYPE, N.FISH_NAME,
        rank() over (partition by FISH_TYPE order by LENGTH desc) as RN,
        LENGTH
from FISH_INFO as I
left join FISH_NAME_INFO as N on I.FISH_TYPE = N.FISH_TYPE
)

select ID, FISH_NAME, LENGTH
from tmp
where tmp.RN = 1
order by ID;
