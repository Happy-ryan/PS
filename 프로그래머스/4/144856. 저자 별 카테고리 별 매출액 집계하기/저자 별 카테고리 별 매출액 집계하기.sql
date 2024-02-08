-- 코드를 입력하세요
# 2022년 1월 판매 데이터 기준
# 저자별 & 카테고리별 매출액
# 저자ID 오름차순 / 카테고리 내림차순
# 저자이름으로 group by 하지 않은 이유: 혹시 동명이인이 있을 수 있으므로 id로 group by 진행
# 이렇게 생각할거면 3개를 group by하면 된다.
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

select B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
from BOOK B
inner join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
inner join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
group by B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
order by B.AUTHOR_ID asc, B.CATEGORY desc;