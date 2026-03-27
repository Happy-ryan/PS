# 자동차의 종류 - 세단, suv
# 2022년 11월 1일 ~ 2022년 11월 30일까지 대여 가능
# 30일간의 대여금액이 50만원 이상, 200만원 미만만 출력!
# 대여금액 내림차순, 자동차 종류 오름차순, 자동차id 내림차순
# history에서 car_id 중복이 존재 > end_date가 가장 큰 것만 나오도록!

# temp - [2022-11-01 ~ 2022-11-30]에 대여가능한 CAR_ID 추출
# car_id가 중복된 존재..그래서 max집계 함수 사용해서 가장 최근 날짜만 추출
with temp as (
    select CAR_ID, max(END_DATE) as END_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    group by CAR_ID
    having year(max(END_DATE)) <= 2022 and month(max(END_DATE)) <= 10
),
# temp2 대여가능한 것 중에서 CAR_TYPE이 SUV와 세단인 CAR의 CAR_ID, TYPE, DAILY_FEE
temp2 as (
    select T.CAR_ID, C.CAR_TYPE, C.DAILY_FEE
    from temp T
    inner join CAR_RENTAL_COMPANY_CAR C on T.CAR_ID = C.CAR_ID
    where C.CAR_TYPE in ('SUV', '세단')
),
# temp3 대여가능한 SUV, 세단의 할인률을 구하기 위해서 join한 후에 계산
temp3 as (
    select T2.CAR_ID, T2.CAR_TYPE,
            round(T2.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100, 0) as FEE
    from temp2 T2
    inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P on T2.CAR_TYPE = P.CAR_TYPE
    where  P.DURATION_TYPE = '30일 이상'
)

# 50만원 이상, 200만원 미만 출력
select CAR_ID, CAR_TYPE, FEE
from temp3
where FEE between 500000 and 1999999
order by FEE desc, CAR_TYPE asc, CAR_ID desc;




# 자동차 종류 - 세단 / SUV
# 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능
# 30일간 대여 금액이 50만원 이상 200만원 미만 >>
# >> 30일 대여하는 것을 default로 잡음!! >  '30일간의 대여 금액'이 50만원 이상 200만원 미만

# 자동차ID / 종류 / 대여금액(FEE)
# 대여금액 내림차순 / 자동차 종류 오름차순 / 자동차 ID 내림차순

# 세단, SUV 중 대여가능한 자동차 ID 뽑기
# 11월 이후 대여 가능 > 대여 마감일이 10월 말을 의미함!!
# 대여기록에는 중복이 존재함 주의해야함!!
with tmp as (
    select H.CAR_ID, C.CAR_TYPE, max(END_DATE)
    from CAR_RENTAL_COMPANY_CAR as C
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY as H on H.CAR_ID = C.CAR_ID
    where C.CAR_TYPE regexp 'SUV|세단'
    group by H.CAR_ID, C.CAR_TYPE
    having year(max(END_DATE)) <= 2022 and month(max(END_DATE)) <= 10
), tmp2 as (
    select T.CAR_ID, T.CAR_TYPE,
            round(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100, 0) as FEE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN as P
    inner join tmp as T on P.CAR_TYPE = T.CAR_TYPE
    inner join CAR_RENTAL_COMPANY_CAR as C on P.CAR_TYPE = C.CAR_TYPE
    where P.DURATION_TYPE ='30일 이상' and
        round(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100, 0) between 500000 and 1999999
    order by FEE desc, CAR_TYPE asc, CAR_ID desc
)

select *
from tmp2;

# 자동차 종류 - 세단, SUV
# 2022년 11월 1일  ~ 2022년 11월 30일 대여 가능
# 30일간의 대여금액이 50만원 ~ 200만원 미만 > 대여금액
# 대여금액기준 내림차순 / 자동차종류 오름차순 / ID 기준

# 대여기록이 없으면 빌릴 수 있는 것 / 있으면 마지막 대여일이 < 20221101 보다 작아야함.
# 차id를 모두 살려야함

# 렌탈 불가능한 차 : 11월에 한 번이라도 대여가 되면 불가능!!
# case1. 11/1 ~[ (시작) 11/30 ]
# case2. [ 11/1 (종료) ] ~ 11/30 
# 시작일이 11월 말보다 전이고, 종료일이 11월 시작보다 뒤라면 무조건 11월에 걸쳐 있음
WITH impossible_car AS (
    SELECT DISTINCT CAR_ID  # 중복제거
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    -- 11월 한 달 동안 조금이라도 대여 중인 차들을 추출
    WHERE START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01'
),
possible_car AS (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE
    FROM CAR_RENTAL_COMPANY_CAR
    -- 'impossible_car' 테이블의 'CAR_ID' 컬럼 값을 리스트로 전달
    WHERE CAR_ID NOT IN (SELECT CAR_ID FROM impossible_car) 
      AND CAR_TYPE IN ('세단', 'SUV')
)

SELECT P.car_id, P.car_type,
        round(P.DAILY_FEE * 30 * (100 - PL.DISCOUNT_RATE) / 100, 0) as FEE
FROM possible_car as P
inner join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as PL ON P.CAR_TYPE = PL.CAR_TYPE
where PL.DURATION_TYPE = '30일 이상' and
        P.DAILY_FEE * 30 * (100 - PL.DISCOUNT_RATE) / 100 between 500000 and 1999999
order by FEE desc, P.CAR_TYPE asc, P.CAR_ID desc;
