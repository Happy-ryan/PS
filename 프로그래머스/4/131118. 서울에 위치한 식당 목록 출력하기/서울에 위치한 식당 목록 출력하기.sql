# 서울에 위치한 식당 ID,이름...
# 리뷰 평균점수 세수점 세번째 자리에서 반올림 = 2자리까지 표시
# 평균점수 내림차순 -> 즐겨찾기 내림차순

select T.REST_ID, T.REST_NAME, T.ADDRESS, round(avg(R.REVIEW_SCORE), 2) as REVIEW_SCORE
from REST_INFO as T 
join REST_REVIEW as R on T.REST_ID = R.REST_ID
where T.ADDRESS like '서울특별시%'
order by R.REVIEW_SCORE desc, T.FAVORITES desc;
















SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS,
        ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I
-- NUll값이 존재하지 않음. 공통된 REST_ID = 35만 결과로 출력됨.
-- inner join에 해당함.
INNER JOIN REST_REVIEW R ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE "서울%"
-- REST_ID 35의 REVIWE SCORE가 AVG 집계함수로 들어가기 위해서 GROUP BY로 묶음.
GROUP BY R.REST_ID
ORDER BY SCORE DESC, I.FAVORITES DESC;

SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS,
        ROUND(AVG(R.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I
-- NUll값이 존재하지 않음. 공통된 REST_ID = 35만 결과로 출력됨.
-- inner join에 해당함.
INNER JOIN REST_REVIEW R ON I.REST_ID = R.REST_ID
WHERE I.ADDRESS LIKE '서울%'
-- REST_ID 35의 REVIWE SCORE가 AVG 집계함수로 들어가기 위해서 GROUP BY로 묶음.
GROUP BY I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS
ORDER BY SCORE DESC, I.FAVORITES DESC;




# 서울에 위치한 식당 / 식당id, 이름, 음식 종류, 즐겨찾기 수, 주소, 리뷰평균
# 리뷰평균점수는 세번째자리에서 반올림 
# 평균점수 기준으로 내림차순 정렬, 평균점수가 같다면 즐겨찾기수 기준 내림차순
with temp as (
    select REST_ID, REST_NAME, FOOD_TYPE, ADDRESS, FAVORITES	
    from REST_INFO
    where ADDRESS like '서울%'
), temp2 as (
    select REST_ID, round(avg(REVIEW_SCORE), 2) as SCORE
    from REST_REVIEW
    group by REST_ID
)

select T1.REST_ID, T1.REST_NAME, T1.FOOD_TYPE, T1.FAVORITES, T1.ADDRESS, T2.SCORE
from temp T1
inner join temp2 T2 on T1.REST_ID = T2.REST_ID
order by T2.SCORE desc, T1.FAVORITES	desc;


# 서울 / 평균리뷰점수 / 세번째 반올림 / 평균 내림차순 / 즐겨찾기 내림차순

with temp as (
    select REST_ID, round(avg(REVIEW_SCORE), 2) as SCORE 
    from REST_REVIEW
    group by REST_ID
), temp2 as (
    select I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, T.SCORE as SCORE
    from temp T
    inner join REST_INFO I on T.REST_ID = I.REST_ID
    where I.ADDRESS like '서울%'
)

select *
from temp2
order by SCORE desc, FAVORITES desc;