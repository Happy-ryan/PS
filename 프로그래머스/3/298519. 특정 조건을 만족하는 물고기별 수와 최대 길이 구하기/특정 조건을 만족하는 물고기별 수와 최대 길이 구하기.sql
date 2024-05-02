-- 코드를 작성해주세요
-- 평균길이 33cm 이상 > 물고기 종류별로 구분 > 잡은수, 최대길이, 물고기의 종류를 출력
-- 물고기의 종류에 대해서 오름차순
-- 10cm이하 물고기들은 10cm로 취급

-- 1. null이거나 10cm이하의 길이들은 10으로 변경해줘야한다.
with tmp as (
    select ID, FISH_TYPE, if(LENGTH <= 10 or LENGTH is null, 10, LENGTH) as LENGTH
    from FISH_INFO
)

select count(ID) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE
from tmp
group by FISH_TYPE
having avg(LENGTH) >= 33
order by FISH_TYPE;