-- 코드를 입력하세요
# 세단 중 10월에 대여를 시작한 기록이 있는 자동자id
# 자동차id 리스트는 중복이 없어야함. > 대여시작일을 최근으로 업데이트를 하는것!
# 자동차id 기준 내림차순
with temp as (
    select CAR_ID, max(START_DATE) as START_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by CAR_ID
    having timestampdiff(day, '2022-10-01', START_DATE) + 1 >= 1
)

select T.CAR_ID
from temp T
inner join CAR_RENTAL_COMPANY_CAR C on T.CAR_ID = C.CAR_ID
where C.CAR_TYPE in ('세단')
order by T.CAR_ID desc;

# 세단 중 10월에 대여를 시작한 기록
# id 중복이 없어야하며, id기준으로 내림차순
# 대여기록, 판매기록 등은 반드시 id의 중복이 있으니 주의해라!
with temp as (
    select CAR_ID, max(START_DATE) as START_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by CAR_ID
    having year(START_DATE) = 2022 and month(START_DATE) = 10
)
select T.CAR_ID
from temp T
inner join CAR_RENTAL_COMPANY_CAR C on T.CAR_ID = C.CAR_ID
where C.CAR_TYPE = '세단'
order by T.CAR_ID desc;