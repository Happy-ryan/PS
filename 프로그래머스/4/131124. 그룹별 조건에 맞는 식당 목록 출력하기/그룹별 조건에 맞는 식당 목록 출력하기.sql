-- 코드를 입력하세요
# 리뷰를 가장 많이한 작성한 회원의 리뷰 조회
# REST_REVIEW 보면 id당 리뷰 스코어가 산재되어있는 상태이다. 아까 5월의 매출 문제와 완전 같은 상황
# 따라서 MEMBER_ID별로 리뷰스코어를 합산한 후에 가장 많은 리뷰를 가진 1명의 사람을 뽑는다.
# 그 사람의 MEMBER_ID를 바탕으로 REST_REVIEW, MEMBER_PROFILE과 join하여 필요한 컬럼 가져온다.
# 리뷰 작성일 오름차순, 리뷰 텍스트 기준 오름차순

with score as (
    select MEMBER_ID, sum(REVIEW_SCORE) as REVIEW_SCORE
    from REST_REVIEW
    group by MEMBER_ID
    order by REVIEW_SCORE desc
    limit 1
)

select P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE P 
inner join REST_REVIEW R on P.MEMBER_ID = R.MEMBER_ID
inner join score S on P.MEMBER_ID = S.MEMBER_ID
order by R.REVIEW_DATE asc, R.REVIEW_TEXT asc;

# 풀이2 - 윈도우 함수 row_number() 사용해보기
# score의 합계로 1순위
with temp as (
    select MEMBER_ID,
        row_number() over (order by sum(REVIEW_SCORE) desc) as rn
    from REST_REVIEW
    group by MEMBER_ID
    limit 1
)

select P.MEMBER_NAME, R.REVIEW_TEXT, date_format(R.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from MEMBER_PROFILE P 
inner join REST_REVIEW R on P.MEMBER_ID = R.MEMBER_ID
inner join temp T on P.MEMBER_ID = T.MEMBER_ID
order by R.REVIEW_DATE asc, R.REVIEW_TEXT asc;






