-- 코드를 작성해주세요

-- 월별(group by) 잡은 물고기의 수
-- 월 기준 오름차순

select count(ID) as FISH_COUNT, month(TIME) as MONTH
from FISH_INFO
group by month(TIME)
order by month(TIME) asc;