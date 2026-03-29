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


# 2022.10.16에 대여 > 대여중 / 대여아니면 대여가능
# history라서 car_id가 많음...
select car_id,
        case
            when sum(
                    case
                        when '2022-10-16' between START_DATE and END_DATE then 1
                        else 0
                    end ) > 0 then '대여중'
            else '대여 가능'
        end as 'AVAILABILITY'
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc;

with tmp as (
    select *, case
                when '2022-10-16' between START_DATE and END_DATE then 1 # 대여중
                else 0
            end as 'CHK'
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
)

select car_id, if(sum(CHK) > 0, '대여중', '대여 가능') as 'AVAILABILITY'
from tmp
group by car_id
order by car_id desc;

# 2022-10-16 대여중인 자동차의 경우 대여 / 아니면 대여 가능
# 반납날짜가 2022-1016이여도 대여중
# 자동차 아이디 기준 내림차순
# history에는 분명 다양한 차가 있을 것. 이때를 어케 특정하면 좋을까?

# start_date를 방문일이라고 생각해보자
# 중복방문제거
-- STEP 1: 같은 차, 같은 날 중복 제거
WITH deduped AS (
    SELECT DISTINCT
        car_id,
        START_DATE
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
),

-- STEP 2: LAG로 이전 대여일 가져오고, TIMESTAMPDIFF로 간격 계산
lagged AS (
    SELECT
        car_id,
        START_DATE,
        LAG(START_DATE) OVER (
            PARTITION BY car_id
            ORDER BY START_DATE
        ) AS prev_date,
        TIMESTAMPDIFF(
            DAY,
            LAG(START_DATE) OVER (
                PARTITION BY car_id
                ORDER BY START_DATE
            ),
            START_DATE
        ) AS day_diff
    FROM deduped
),

-- STEP 3: 간격이 1일이 아니면 새 그룹 플래그
streak_flags AS (
    SELECT
        car_id,
        START_DATE,
        day_diff,
        CASE
            WHEN day_diff = 1 THEN 0
            ELSE 1
        END AS is_new_streak
    FROM lagged
),

-- STEP 4: 누적합으로 그룹 ID 생성
tmp4 AS (
    SELECT
        car_id,
        START_DATE,
        SUM(is_new_streak) OVER (
            PARTITION BY car_id
            ORDER BY START_DATE
        ) AS grp_id
    FROM streak_flags
),

-- STEP 5: 그룹별 집계
tmp5 AS (
    SELECT
        car_id,
        grp_id,
        MIN(START_DATE) AS streak_start,
        MAX(START_DATE) AS streak_end,
        COUNT(*)         AS streak_days
    FROM tmp4
    GROUP BY car_id, grp_id
)

SELECT
    car_id,
    streak_start,
    streak_end,
    streak_days
FROM tmp5
WHERE streak_days >= 2
ORDER BY car_id, streak_days;

# 연속 2일 이상 방문한 차량의 시작 / 끝 / 얼마나 연속 방문했는지
with tmp1 as (
    select distinct car_id, 
            start_date
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
), tmp2 as (
    select *,
            lag(start_date) over (partition by car_id order by start_date) as prev_date
    from tmp1
), tmp3 as (
    select *,
            case
                when timestampdiff(day, prev_date, start_date) = 1 then 0 # 연속된 그룹을 만들고자함 > 그것에 누적합을 사용할 것 > 연속되면 합을 올리면 안되니까 0
                else 1
            end as new
    from tmp2
),
# sum(feild) over (partition by orde by)  <- 누적합!!
tmp4 as( 
    select car_id,
            start_date,
            sum(new) over (partition by car_id order by start_date) as gr_id
    from tmp3
), 
tmp5 as (
    select  car_id, 
            gr_id,
            min(start_date) as min_start,
            max(start_date) as max_start,
            count(*) as long_date
    from tmp4
    group by car_id, gr_id
)

select *
from tmp2;

with tmp as (
    select car_id,
            start_date,
            end_date,
            lag(end_date) over (partition by car_id order by start_date, end_date) as prev_end_dt
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
),tmp2 as (
    select car_id,
            start_date,
            end_date,
            prev_end_dt,
            case
                when prev_end_dt is null then start_date
                when prev_end_dt > start_date then prev_end_dt
                else start_date
            end as real_start_dt
    from tmp
    
), tmp3 as (
    select car_id,
        start_date,
        end_date,
        real_start_dt,
        greatest(
            timestampdiff(minute, real_start_dt, end_date), 0
        ) as net_minutes
    from tmp2
), tmp4 as (
    SELECT
    car_id,
    SUM(net_minutes)          AS total_net_minutes,
    SUM(net_minutes) / 60     AS total_net_hours
FROM tmp3
GROUP BY car_id
ORDER BY car_id
)

select *
from tmp4;

SET @dt = '2022-10-16';
WITH rental_status AS (
    -- STEP 1: 각 기록마다 기준일 포함 여부를 0/1 로 표시
    SELECT
        CAR_ID,
        CASE
            WHEN START_DATE <= @dt
             AND  @dt  <= END_DATE
            THEN 1 # 한 대여기록의 시작일과 종료일 사이에 @dt가 존재한다면 대여 중인것!!
            ELSE 0
        END AS is_active
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
),

car_status AS (
    -- STEP 2: CAR_ID 로 묶어서 기록 중 하나라도 is_active = 1 이면 대여중
    SELECT
        CAR_ID,
        MAX(is_active) AS is_active
    FROM rental_status
    GROUP BY CAR_ID
)

-- STEP 3: 최종 출력
SELECT
    CAR_ID,
    CASE
        WHEN is_active = 1 THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM car_status
ORDER BY CAR_ID DESC;
