-- 코드를 입력하세요
# 2022년 1월 판매 데이터 기준
# 저자별 & 카테고리별 매출액
# 저자ID 오름차순 / 카테고리 내림차순
with temp as (
    select B.AUTHOR_ID, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
    from BOOK B
    inner join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
    inner join BOOK_SALES S  on B.BOOK_ID = S.BOOK_ID
    where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
    group by AUTHOR_ID, CATEGORY
    order by B.AUTHOR_ID asc, B.CATEGORY desc
)


select temp.AUTHOR_ID, A.AUTHOR_NAME, temp.CATEGORY, temp.TOTAL_SALES
from temp
inner join AUTHOR A on temp.AUTHOR_ID = A.AUTHOR_ID ;

