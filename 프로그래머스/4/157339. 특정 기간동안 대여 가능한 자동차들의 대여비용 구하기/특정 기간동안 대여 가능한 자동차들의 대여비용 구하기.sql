# 자동차의 종류 - 세단, suv
# 2022년 11월 1일 ~ 2022년 11월 30일까지 대여 가능
# 30일간의 대여금액이 50만원 이상, 200만원 미만만 출력!
# 대여금액 내림차순, 자동차 종류 오름차순, 자동차id 내림차순
# history에서 car_id 중복이 존재 > end_date가 가장 큰 것만 나오도록!
with temp as (
    select CAR_ID, max(END_DATE) as END_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    group by CAR_ID
    having year(max(END_DATE)) <= 2022 and month(max(END_DATE)) <= 10
), temp2 as (
    select T.CAR_ID, T.END_DATE, C.CAR_TYPE, C.DAILY_FEE
    from temp T
    inner join CAR_RENTAL_COMPANY_CAR C on T.CAR_ID = C.CAR_ID
    where C.CAR_TYPE in ('SUV', '세단')
), temp3 as (
    select T2.CAR_ID, T2.CAR_TYPE, T2.DAILY_FEE, P.DISCOUNT_RATE
    from temp2 T2
    inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P on T2.CAR_TYPE = P.CAR_TYPE
    where  P.DURATION_TYPE = '30일 이상'
)


select CAR_ID, CAR_TYPE, round(DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100, 0) as FEE
from temp3
where round(DAILY_FEE * 30 * (100 - DISCOUNT_RATE) / 100, 0) between 500000 and 1999999
order by FEE desc, CAR_TYPE asc, CAR_ID desc;

/*
CAR_ID  CAR_TYPE    FEE
3   세단  1518000
23  세단  1380000
*/