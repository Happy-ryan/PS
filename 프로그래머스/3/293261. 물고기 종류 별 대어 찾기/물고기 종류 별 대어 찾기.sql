-- 코드를 작성해주세요
-- 종류별 가장 큰 물고기를 찾아라
-- ID기준 오름차순

# with tmp as (
# select  I.ID, I.FISH_TYPE, N.FISH_NAME,
#         rank() over (partition by FISH_TYPE order by LENGTH desc) as RN,
#         LENGTH
# from FISH_INFO as I
# left join FISH_NAME_INFO as N on I.FISH_TYPE = N.FISH_TYPE
# )

# select ID, FISH_NAME, LENGTH
# from tmp
# where tmp.RN = 1
# order by ID;
















# 물고기 종류별로 가장 큰 물고기의 ID, 이름, 길이
# 물고기 ID 오름차순

with tmp as ( 
    select I.FISH_TYPE, N.FISH_NAME AS FISH_NAME, max(I.LENGTH) as LENGTH
from FISH_INFO AS I
inner join FISH_NAME_INFO AS N on I.FISH_TYPE = N.FISH_TYPE
where I.LENGTH is not null # null이 아닌 물고기 중
group by I.FISH_TYPE, N.FISH_NAME
)
select I.ID, T.FISH_NAME, T.LENGTH
from tmp AS T
inner join FISH_INFO AS I on T.FISH_TYPE = I.FISH_TYPE
where I.LENGTH = T.LENGTH
order by I.ID;

