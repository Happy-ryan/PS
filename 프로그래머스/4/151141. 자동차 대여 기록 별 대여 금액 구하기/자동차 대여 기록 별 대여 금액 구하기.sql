-- 코드를 입력하세요
# 자동차의 종류 - 트럭 / 대여기록 별로 대여금액 > 대여 기록id, 대여금액 리스트 출력
# 대여금액 기준 내림차순 / 기록id 내림차순
with temp as (
    select H.HISTORY_ID, timestampdiff(day, H.START_DATE, H.END_DATE) + 1 as DAY,
        case
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 >= 90 then '90일 이상'
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 between 30 and 89 then '30일 이상'
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 between 7 and 29 then '7일 이상'
        else null
        end as DURATION,
        C.DAILY_FEE * (timestampdiff(day, H.START_DATE, H.END_DATE) + 1) as TOTAL_FEE,
        C.CAR_TYPE
    from CAR_RENTAL_COMPANY_CAR C
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY H on C.CAR_ID = H.CAR_ID
    where C.CAR_TYPE = '트럭'
)

select T.HISTORY_ID,
    round(T.TOTAL_FEE * ((100 - if(P.DURATION_TYPE is null, 0, P.DISCOUNT_RATE)) / 100), 0) as FEE
from temp T
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
        on T.CAR_TYPE = P.CAR_TYPE and T.DURATION = P.DURATION_TYPE
order by FEE desc, HISTORY_ID desc;