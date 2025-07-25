# -- 코드를 입력하세요
# # 2022년 1월 판매 데이터 기준
# # 저자별 & 카테고리별 매출액
# # 저자ID 오름차순 / 카테고리 내림차순
# # 저자이름으로 group by 하지 않은 이유: 혹시 동명이인이 있을 수 있으므로 id로 group by 진행
# # 그런데 생각할거면 3개(id, name, category)를 group by하면 된다.
# with temp as (
#     select B.AUTHOR_ID, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
#     from BOOK B
#     inner join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
#     inner join BOOK_SALES S  on B.BOOK_ID = S.BOOK_ID
#     where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
#     group by AUTHOR_ID, CATEGORY
#     order by B.AUTHOR_ID asc, B.CATEGORY desc
# )

# select temp.AUTHOR_ID, A.AUTHOR_NAME, temp.CATEGORY, temp.TOTAL_SALES
# from temp
# inner join AUTHOR A on temp.AUTHOR_ID = A.AUTHOR_ID;

# -- 
# select B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
# from BOOK B
# inner join AUTHOR A on B.AUTHOR_ID = A.AUTHOR_ID
# inner join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
# where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
# group by B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
# order by B.AUTHOR_ID asc, B.CATEGORY desc;

# # 2022년 1월 - 저자별, 카테고리별 매출액
# # 저자id, 저자명, 카테고리, 매출애
# with temp as (
#     select B.CATEGORY, B.AUTHOR_ID, sum(B.PRICE * S.SALES) as TOTAL_SALES
#     from BOOK B
#     inner join BOOK_SALES S on B.BOOK_ID = S.BOOK_ID
#     where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
#     group by B.CATEGORY, B.AUTHOR_ID
# )

# select T.AUTHOR_ID, A.AUTHOR_NAME, T.CATEGORY, T.TOTAL_SALES
# from temp T
# inner join AUTHOR A on A.AUTHOR_ID = T.AUTHOR_ID
# order by A.AUTHOR_ID asc, T.CATEGORY desc;













# # 2022년 1월 - 저자별 / 카테고리별 매출액 (판매량 * 판매가)
# # 저자, 저자명, 카테고리, 매출액
# # 저자ID 오름차순 / 카테고리별 내림차순

# # sum(S.SALES * B.PRICE)
# # price 저자별 / 카테고리별 가격이 다르기 때문에 안에서 곱해야함!
# with tmp as (
#     select A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(S.SALES * B.PRICE) as TOTAL_SALES
#     from BOOK as B
#     inner join AUTHOR as A on A.AUTHOR_ID = B.AUTHOR_ID	
#     inner join BOOK_SALES as S on B.BOOK_ID = S.BOOK_ID
#     where year(S.SALES_DATE) = 2022 and month(S.SALES_DATE) = 1
#     group by B.CATEGORY, A.AUTHOR_ID, A.AUTHOR_NAME
#     order by A.AUTHOR_ID asc, B.CATEGORY desc
# )

# select *
# from tmp;

# # 카테고리 / 저자 ID - price가 다른게 존재
# # price 밖에서 곱하면 price가 두 개 이상일 때 하나 죽어버림
# # sum(S.SALES) * B.PRICE 하면 안된다!!

# with tmp as (
#     select B.CATEGORY, B.AUTHOR_ID, sum(S.SALES * B.PRICE) as SALES
#     from BOOK as B
#     inner join BOOK_SALES as S on B.BOOK_ID = S.BOOK_ID
#     where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
#     group by B.CATEGORY, B.AUTHOR_ID
# )

# select A.AUTHOR_ID, A.AUTHOR_NAME, T.CATEGORY, T.SALES as TOTAL_SALES
# from tmp as T
# inner join AUTHOR as A on T.AUTHOR_ID = A.AUTHOR_ID
# order by A.AUTHOR_ID asc, T.CATEGORY desc;


# 2022년 1월 기준 저자별 / 카테고리별 매출액(판매량 * 판매가)
# 저자, 저자명, 카테고리, 매출액 리스트 출력
# 저자id 오름차순 / 카테도리 내림차순

# 1) 저자별 / 카테고리별 판매량 계산
with tmp1 as (
    select sum(S.sales * B.price) as total_sales, author_id, category 
    from BOOK as B
    inner join BOOK_SALES as S on B.book_id = S.book_id
    where year(S.sales_date) = 2022 and month(S.sales_date) = 1
    group by author_id, category
    
)

select T1.author_id, A.author_name, T1.category, T1.total_sales
from tmp1 as T1
inner join AUTHOR as A on A.AUTHOR_ID = T1.AUTHOR_ID
order by AUTHOR_ID asc, CATEGORY desc;