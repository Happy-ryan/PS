-- 코드를 입력하세요
-- 2022년 10월 16일에 대여 중인 자동차인 경우 '대여중' 이라고 표시하고
-- 대여 중이지 않은 자동차인 경우 '대여 가능'을 표시하는 컬럼(컬럼명: AVAILABILITY)을 추가
-- 반납 날짜가 2022년 10월 16일인 경우에도 '대여중'
--  자동차 ID를 기준으로 내림차순


with temp as (
    select CAR_ID, START_DATE, END_DATE
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    order by CAR_ID desc 
), temp2 as (
    select CAR_ID, 
        if(timestampdiff(day, '2022-10-16', END_DATE) < 0  or 
           timestampdiff(day, '2022-10-16', START_DATE) > 0,'대여 가능', '대여중') as AVAILABILITY
    from temp
    group by CAR_ID
    order by CAR_ID desc
)

select *
from temp2;
# 2022년 10월 16일에 대여중이 자동차의 경우 대여중 / 대여중이지 않는 경우 대여가능 컬럼 추가
# 반납날짜가 20221016에도 대여중
# 자동차id 기준 내림차순 정렬

# 같은 자동차 기록 중 가장 최신 기록이 필요
with tmp1 as (
    select car_id, 
    start_date, end_date,
    row_number() over (partition by CAR_ID order by start_date desc, end_date desc) as rn
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

# timestampdiff(기준, 시간1, 시간2) = 시간2 - 시간1
select car_id, start_date, end_date,
        if('2022-10-16' between start_date and end_date,'대여중', '대여가능') as AVAILABILITY
from tmp1
where rn = 1 and '2022-10-16' between start_date and end_date;

with tmp1 as (
    select CAR_ID, group_concat(if('2022-10-16' between start_date and end_date, "대여중", "대여 가능")) as text
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    group by CAR_ID
)

select car_id, if(text like '%대여중%', "대여중", "대여 가능") as AVAILABILITY
from tmp1
order by car_id desc;
