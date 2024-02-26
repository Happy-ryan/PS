-- 코드를 입력하세요
# 공간을 둘 이상 등록한 사람을 헤비유저
# 헤비유저가 등록한 공간의 정보를 아이디순으로 
with temp as (
    select HOST_ID
    from PLACES
    group by HOST_ID
    having count(*) >= 2
)

select ID, NAME, HOST_ID
from PLACES 
where HOST_ID in (select HOST_ID from temp)
order by ID asc;