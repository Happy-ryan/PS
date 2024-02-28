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