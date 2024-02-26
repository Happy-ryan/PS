-- 코드를 입력하세요
# 공간을 둘 이상 등록한 사람을 헤비유저
# 헤비유저가 등록한 공간의 정보를 아이디순으로 
with temp as (
    select HOST_ID, count(*) as COUNT
    from PLACES
    group by HOST_ID
    having COUNT >= 2
)

select P.ID, P.NAME, P.HOST_ID
from temp T
inner join PLACES P on T.HOST_ID = P.HOST_ID
order by P.ID asc;