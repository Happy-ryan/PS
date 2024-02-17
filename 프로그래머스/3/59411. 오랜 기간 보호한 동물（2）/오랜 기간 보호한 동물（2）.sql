-- 코드를 입력하세요
# 입양을 간 동물 중
# 보호기간이 가장 길었던 동물 두마리의 아이디, 이름
# 보호기간 긴 순으로 내림차순
# 보호기간 = 입양일 - 보호시작일
with temp as (
    select I.ANIMAL_ID, I.NAME, timestampdiff(day,I.DATETIME, O.DATETIME)
    from ANIMAL_INS I
    inner join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
    order by timestampdiff(day,I.DATETIME, O.DATETIME) desc
    limit 2
)

select ANIMAL_ID, NAME
from temp;