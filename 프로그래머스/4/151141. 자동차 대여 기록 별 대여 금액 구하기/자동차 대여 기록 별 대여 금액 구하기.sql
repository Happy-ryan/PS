-- 코드를 입력하세요
# 자동차의 종류 - 트럭 / 대여기록 별로 대여금액 > 대여 기록id, 대여금액 리스트 출력
# 대여금액 기준 내림차순 / 기록id 내림차순

with temp as (
    select H.HISTORY_ID,
        case
            when timestampdiff(day, H.START_DATE, H.END_DATE) < 7 then null
            when timestampdiff(day, H.START_DATE, H.END_DATE) < 30 then '7일 이상'
            when timestampdiff(day, H.START_DATE, H.END_DATE) < 90 then '30일 이상'
            else '90일 이상'
        end as DURATION_TYPE,
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
        on T.CAR_TYPE = P.CAR_TYPE and T.DURATION_TYPE = P.DURATION_TYPE
order by FEE desc, T.HISTORY_ID desc;



# 자동차 종류 - 트럭 / 자동차 대여기록에 대해서 대여기록별로 대여금액을 구하기
# 대여기록id, 대여금액 리스트 / 대여금액 기준 내림차순, 기록id기준 내림차순

with temp as (
    select H.CAR_ID, H.HISTORY_ID, C.CAR_TYPE,
    case
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 7 then null
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 30 then '7일 이상'
        when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 90 then '30일 이상'
        else '90일 이상' 
    end as DURATION_TYPE,
    (timestampdiff(day, H.START_DATE, H.END_DATE) + 1) * C.DAILY_FEE as TOTAL_FEE
    from CAR_RENTAL_COMPANY_CAR C
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY H on C.CAR_ID = H.CAR_ID
    where C.CAR_TYPE = '트럭'
)

select T.HISTORY_ID,
    round((T.TOTAL_FEE * (100 - ifnull(P.DISCOUNT_RATE, 0)) / 100), 0) as FEE
from temp T
-- temp에 7일 이하는 null로 들어감..그래서 inner join을 하면 사라짐
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
    on T.CAR_TYPE = P.CAR_TYPE and T.DURATION_TYPE = P.DURATION_TYPE
    order by FEE desc, T.HISTORY_ID desc;


# 대여기록별 대여금액 / 기록id, 대여금액 리스트 / 대여 금액 기준 내림차순 / id 기준 내림차순
# 자동차의 종류가 '트럭'
with temp as (
    select H.HISTORY_ID, H.CAR_ID, C.CAR_TYPE, C.DAILY_FEE,
            timestampdiff(day, H.START_DATE, H.END_DATE) + 1 as DURATION,
            case
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 7 then null
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 30 then '7일 이상'
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 < 90 then '30일 이상'
                else '90일 이상'
            end as DURATION_TYPE              
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    inner join CAR_RENTAL_COMPANY_CAR C on H.CAR_ID = C.CAR_ID
    where C.CAR_TYPE = '트럭'
)

select T.HISTORY_ID, round(((100 - ifnull(discount_rate, 0)) * T.DURATION * T.DAILY_FEE) / 100 , 0) as FEE
from temp T
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P on T.CAR_TYPE = P.CAR_TYPE and T.DURATION_TYPE = P.DURATION_TYPE
order by FEE desc, T.HISTORY_ID desc;

# HISTORY_ID	FEE
# 724	6336960
# 681	5356240
# 630	4791360
# 558	4404960
# 653	3793160
# 722	2909040
# 594	1888600
# 680	1524750
# 714	1118150
# 591	1118150
# 556	813200
# 610	672000
# 676	568000
# 527	535000
# 720	532000
# 710	532000
# 701	504000
# 640	428000
# 641	426000
# 628	426000
# 623	336000
# 602	336000
# 673	321000
# 631	321000
# 654	284000
# 618	214000
# 586	214000
# 581	214000
# 546	214000
# 716	140000
# 711	107000
# 705	107000
# 627	107000
# 524	107000

# 자동차 종류 - 트럭 / 대여기록별 대여금액 구하기 / 대여금액 기준 내림차순 / 대여 기록id기준 내림차순
with temp as (
    select H.HISTORY_ID,
        C.DAILY_FEE * (timestampdiff(day, START_DATE, END_DATE) + 1) as TOTAL_FEE,
        case
            when timestampdiff(day, START_DATE, END_DATE) + 1 < 7 then null
            when timestampdiff(day, START_DATE, END_DATE) + 1 < 30 then '7일 이상'
            when timestampdiff(day, START_DATE, END_DATE) + 1 < 90 then '30일 이상'
            else '90일 이상'
        end as DURATION_TYPE,
        C.CAR_TYPE
    from CAR_RENTAL_COMPANY_CAR C
    inner join CAR_RENTAL_COMPANY_RENTAL_HISTORY H on C.CAR_ID = H.CAR_ID
    where C.CAR_TYPE = '트럭'
    
)

select T.HISTORY_ID, round((T.TOTAL_FEE * (100 - ifnull(P.discount_rate, 0)) / 100) ,0) as FEE
from temp T
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN P 
        on T.DURATION_TYPE = P.DURATION_TYPE and T.CAR_TYPE = P.CAR_TYPE
order by FEE desc, HISTORY_ID desc;

-- 자동차의 종류 = 트럭 / 대여 기록 별 대여금액 / 기록ID
-- 대여 금액 기준 내림차순, ID기준 내림차순
with history as (
    select  H.HISTORY_ID, C.CAR_TYPE,
            case
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 >= 90 then '90일 이상'
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 >= 30 then '30일 이상'
                when timestampdiff(day, H.START_DATE, H.END_DATE) + 1 >= 7 then '7일 이상'
                else null
            end as DURATION_TYPE,
            C.DAILY_FEE * (timestampdiff(day, H.START_DATE, H.END_DATE) + 1) as TOTAL_FEE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY as H
    left join CAR_RENTAL_COMPANY_CAR as C on H.CAR_ID = C.CAR_ID
    where C.CAR_TYPE = '트럭'
)

select H.HISTORY_ID, round(((100 - ifnull(P.DISCOUNT_RATE, 0)) * H.TOTAL_FEE) / 100, 0) as FEE
from history as H
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as P 
    on H.DURATION_TYPE = P.DURATION_TYPE and P.CAR_TYPE = H.CAR_TYPE
order by FEE desc, H.HISTORY_ID desc;

# 자동차 종류 = 트럭 / 대여기록별 대여금액 계산
# 대여기록ID와 대여금액
# 금액 기준 내림차순 기록ID 내림차순

# step1. 트럭과 대여기록 계산, 하루 빌리는 금액 계산
with tmp as (
    select  H.HISTORY_ID,  I.CAR_TYPE,
            I.DAILY_FEE * (timestampdiff(day,H.START_DATE, H.END_DATE) + 1) as 'TOTAL',
            timestampdiff(day,H.START_DATE, H.END_DATE) + 1 as 'DATE',
            I.DAILY_FEE,
            case
                when timestampdiff(day,H.START_DATE, H.END_DATE) + 1 < 7 then NULL
                when timestampdiff(day,H.START_DATE, H.END_DATE) + 1 < 30 then '7일 이상'
                when timestampdiff(day,H.START_DATE, H.END_DATE) + 1 < 90 then '30일 이상'
                else '90일 이상'
            end as 'DURATION_TYPE'
    from CAR_RENTAL_COMPANY_CAR as I 
    right outer join CAR_RENTAL_COMPANY_RENTAL_HISTORY as H on I.CAR_ID = H.CAR_ID
    where I.CAR_TYPE in ('트럭')
)

# left join했을 때 7미만은 null 상태라서 duration_type이 null 발생. 그런데 null이면 계산 안됨 
# 따라서 ifnull 활용해서 null이 아니라 0이되도록 
select  T.HISTORY_ID,
        round(T.TOTAL * (100 - ifnull(P.DISCOUNT_RATE, 0)) / 100) as 'FEE' 
from tmp as T
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN as P on T.DURATION_TYPE = P.DURATION_TYPE and T.CAR_TYPE = P.CAR_TYPE
order by FEE desc, T.HISTORY_ID desc;