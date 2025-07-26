-- 코드를 입력하세요
# SELECT R1.FOOD_TYPE, R1.REST_ID, R1.REST_NAME, R1.FAVORITES
# FROM REST_INFO R1
# JOIN (
#     SELECT FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
#     FROM REST_INFO
#     GROUP BY FOOD_TYPE
# ) R2 ON R1.FOOD_TYPE = R2.FOOD_TYPE AND R1.FAVORITES = R2.FAVORITES
# ORDER BY R1.FOOD_TYPE DESC;

# select R1.FOOD_TYPE, R1.REST_ID, R1.REST_NAME, R1.FAVORITES
# from REST_INFO R1
# inner join (
#     select FOOD_TYPE, MAX(FAVORITES) AS FAVORITES
#     from REST_INFO
#     group by FOOD_TYPE) R2 on R1.FOOD_TYPE = R2.FOOD_TYPE AND R1.FAVORITES = R2.FAVORITES
# order by R1.FOOD_TYPE desc;

SELECT R.FOOD_TYPE, R.REST_ID, R.REST_NAME, R.FAVORITES
FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
            RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS rn
    FROM REST_INFO
) AS R
WHERE R.rn = 1
ORDER BY R.FOOD_TYPE DESC;

# 음식종류별로 즐겨찾기 수가 가장 많은 식당
# 음식종류 기준 내림차순
with temp as (
    select FOOD_TYPE, max(FAVORITES) as FAVORITES
    from REST_INFO
    group by FOOD_TYPE
)

select T.FOOD_TYPE, REST_ID, REST_NAME, T.FAVORITES
from temp T
inner join REST_INFO R on T.FOOD_TYPE = R.FOOD_TYPE and T.FAVORITES = R.FAVORITES
order by T.FOOD_TYPE desc;

# 각 음식별로 좋아요 1등 - 윈도우
with temp as (
    select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
        row_number() over(partition by FOOD_TYPE order by FAVORITES desc) as rn
    from REST_INFO
    
)

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from temp
where temp.rn = 1
order by FOOD_TYPE desc;

# FOOD_TYPE	REST_ID	REST_NAME	FAVORITES
# 한식	00001	은돼지식당	734
# 중식	00015	만정	20
# 일식	00004	스시사카우스	230
# 양식	00003	따띠따띠뜨	102
# 분식	00008	애플우스	151


# 음식종류별 즐겨찾기가 가장 많은 식당의 음식종류 / ID / 식당이름 / 즐겨차지수 조회
# 음식종류기준 내림차순

# 종류별 > groupby > 가장 많은 limit > row_number

with tmp as (
    select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
            row_number() over (partition by FOOD_TYPE order by FAVORITES desc) as rn
    from REST_INFO
    order by FOOD_TYPE desc
)

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from tmp
where rn = 1;


# 풀이1) 윈도우함수
with tmp as (
    select row_number() over (partition by FOOD_TYPE order by FAVORITES desc) as rn,
           FOOD_TYPE, REST_ID, FAVORITES, REST_NAME
    from REST_INFO
)

select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from tmp
where rn = 1
order by FOOD_TYPE desc;

# 풀이2) 그룹콘캣
with tmp as (
    select substring_index(group_concat(REST_ID order by FAVORITES desc), ',', 1) as REST_ID
    from REST_INFO
    group by FOOD_TYPE
)

select I.FOOD_TYPE, I.REST_ID, I.REST_NAME, I.FAVORITES
from tmp as T
inner join REST_INFO as I on T.REST_ID = I.REST_ID
order by I.FOOD_TYPE desc;