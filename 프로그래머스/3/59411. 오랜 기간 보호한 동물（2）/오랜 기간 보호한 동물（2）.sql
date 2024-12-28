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

# 윈도우함수!!
with temp as (
    select I.ANIMAL_ID, I.NAME, 
        row_number() over (order by timestampdiff(day,I.DATETIME, O.DATETIME) desc) as rn
    from ANIMAL_INS I
    inner join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
)

select ANIMAL_ID, NAME
from temp
where rn = 1 or rn = 2;



# 입양 / 보호기간 가장 길었던 두 마리(limit, row_numebr) id, 이름 조회
# 보호기간이 긴 순으로 조회
# 풀이1 - 윈도우 함수
with temp as (
    select I.ANIMAL_ID, I.NAME,
            row_number() over (order by timestampdiff(day, I.DATETIME, O.DATETIME) + 1 desc) as rn
    from ANIMAL_INS I
    inner join ANIMAL_OUTS O on  I.ANIMAL_ID = O.ANIMAL_ID
)

select ANIMAL_ID, NAME
from temp
where temp.rn = 1 or temp.rn = 2;

# 풀이2 limit
with temp as (
    select I.ANIMAL_ID, I.NAME
    from ANIMAL_INS I
    inner join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
    order by timestampdiff(day, I.DATETIME, O.DATETIME) + 1 desc
    limit 2
)

select *
from temp;





# 입양을 간 동물 중 보호기간이 가장 길었던 동물 두 마리 = limit / row_number() 사용
# 보호기간이 긴 순서로 조회
with tmp as (
select I.ANIMAL_ID, I.NAME,
        row_number() over (order by timestampdiff(day, I.DATETIME, O.DATETIME) + 1 desc) AS rn
from ANIMAL_INS AS I
inner join ANIMAL_OUTS AS O on I.ANIMAL_ID = O.ANIMAL_ID
order by timestampdiff(day, I.DATETIME, O.DATETIME) desc
)
select ANIMAL_ID, NAME
from tmp
where rn = 1 or rn = 2;
