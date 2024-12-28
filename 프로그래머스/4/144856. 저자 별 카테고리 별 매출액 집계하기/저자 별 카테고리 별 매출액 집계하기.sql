-- 코드를 입력하세요
# 2022년 1월 판매 데이터 기준
# 저자별 & 카테고리별 매출액
# 저자ID 오름차순 / 카테고리 내림차순
# 저자이름으로 group by 하지 않은 이유: 혹시 동명이인이 있을 수 있으므로 id로 group by 진행
# 그런데 생각할거면 3개(id, name, category)를 group by하면 된다.
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
inner join AUTHOR A on temp.AUTHOR_ID = A.AUTHOR_ID;

-- 
select B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
from BOOK B
inner join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
inner join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
group by B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
order by B.AUTHOR_ID asc, B.CATEGORY desc;

# 2022년 1월 - 저자별, 카테고리별 매출액
# 저자id, 저자명, 카테고리, 매출애
with temp as (
    select B.CATEGORY, B.AUTHOR_ID, sum(B.PRICE * S.SALES) as TOTAL_SALES
    from BOOK B
    inner join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
    where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
    group by B.CATEGORY, B.AUTHOR_ID
)

select T.AUTHOR_ID, A.AUTHOR_NAME, T.CATEGORY, T.TOTAL_SALES
from temp T
inner join AUTHOR A on A.AUTHOR_ID = T.AUTHOR_ID
order by A.AUTHOR_ID asc, T.CATEGORY desc;













# 2022년 1월 - 저자별 / 카테고리별 매출액 (판매량 * 판매가)
# 저자, 저자명, 카테고리, 매출액
# 저자ID 오름차순 / 카테고리별 내림차순
with tmp as (
    select A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
    from BOOK as B
    inner join AUTHOR as A on A.AUTHOR_ID = B.AUTHOR_ID	
    inner join BOOK_SALES as S on B.BOOK_ID = S.BOOK_ID
    where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
    group by B.CATEGORY, A.AUTHOR_ID, A.AUTHOR_NAME
    order by A.AUTHOR_ID asc, B.CATEGORY desc
)

select *
from tmp;