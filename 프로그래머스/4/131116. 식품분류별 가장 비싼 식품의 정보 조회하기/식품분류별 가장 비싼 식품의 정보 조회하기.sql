-- 코드를 입력하세요
# 식품별 가격 제일 비싼거
# 식품분류 -  '과자', '국', '김치', '식용유' - where
# 식품 가격 기준 내림차순
with temp as (
    select CATEGORY, max(PRICE) as PRICE
    from FOOD_PRODUCT
    group by CATEGORY
    )
    
select P.CATEGORY, P.PRICE, P.PRODUCT_NAME
from FOOD_PRODUCT P
inner join temp T on (P.CATEGORY = T.CATEGORY and P.PRICE = T.PRICE)
where P.CATEGORY in ('과자', '국', '김치', '식용유')
order by P.PRICE desc;

# 각 카테고리별 최대값 가져오기 = substring_index + group_concat
# substring_index(group_concat(P.PRODUCT_NAME order by P.PRICE desc), ',', 1)
select P.CATEGORY, MAX(P.PRICE) as MAX_PRICE, 
       substring_index(group_concat(P.PRODUCT_NAME ORDER BY P.PRICE DESC), ',', 1)
       AS PRODUCT_NAME
from FOOD_PRODUCT P
where P.CATEGORY in ('과자', '국', '김치', '식용유')
group by P.CATEGORY
order by P.PRICE desc;

select CATEGORY, 
       PRICE as MAX_PRICE, 
       PRODUCT_NAME
from FOOD_PRODUCT 
where (CATEGORY, PRICE) in (
    select CATEGORY, max(PRICE)
    from FOOD_PRODUCT 
    where CATEGORY in ('과자', '국', '김치', '식용유')
    group by CATEGORY
)
order by PRICE desc;

# 식품분류별로 가격이 제일 비싼 식품의 정보 얻기
# 식품분류, 과자, 국, 김치, 식용유인경우만 출력!
# 식품 가격 기준 내림차순

with temp as (
    select CATEGORY,PRODUCT_ID,PRODUCT_NAME,PRICE,
        row_number() over(partition by CATEGORY order by PRICE desc) as rn
    from FOOD_PRODUCT
    where CATEGORY regexp '과자|국|김치|식용유'
)

select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME
from temp T
where T.rn = 1
order by MAX_PRICE desc;

with temp as (
    select CATEGORY, max(PRICE) as MAX_PRICE, 
        substring_index(group_concat(PRODUCT_NAME order by PRICE desc), ',', 1) as PRODUCT_NAME
    from FOOD_PRODUCT
    where CATEGORY regexp '과자|국|김치|식용유'
    group by CATEGORY
)

select *
from temp
order by MAX_PRICE desc;

select CATEGORY, group_concat(PRODUCT_NAME order by PRICE desc) as NAME
from FOOD_PRODUCT
where CATEGORY regexp '과자|국|김치|식용유'
group by CATEGORY;

# 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름 조회
# 식품분류 - 과자 / 국 / 김치 / 식용유인 경우만 출력
# 식품 가격을 기준으로 내림차순
with tmp as (
select CATEGORY, max(PRICE) as MAX_PRICE
from FOOD_PRODUCT
where CATEGORY IN ('식용유', '과자', '김치', '국')
group by CATEGORY
)
select R.CATEGORY, T.MAX_PRICE, R.PRODUCT_NAME
from tmp as T
inner join FOOD_PRODUCT as R on T.CATEGORY = R.CATEGORY
where T.MAX_PRICE = R.PRICE
order by T.MAX_PRICE desc;

# row_number()사용해보기
with tmp as (
    select CATEGORY, PRICE, PRODUCT_NAME, 
            row_number() over (partition by CATEGORY order by PRICE desc) as rn
    from FOOD_PRODUCT
    where CATEGORY regexp '식용유|과자|국|김치'
)

select CATEGORY, PRICE, PRODUCT_NAME
from tmp
where rn = 1
order by PRICE desc;

# 각 카테고리별 최대값 가져오기 = substring_index + group_concat
# substring_index(group_concat(P.PRODUCT_NAME order by P.PRICE desc), ',', 1)
select P.CATEGORY, MAX(P.PRICE) as MAX_PRICE, 
       substring_index(group_concat(P.PRODUCT_NAME ORDER BY P.PRICE DESC), ',', 1)
       AS PRODUCT_NAME
from FOOD_PRODUCT P
where P.CATEGORY in ('과자', '국', '김치', '식용유')
group by P.CATEGORY
order by P.PRICE desc;

select CATEGORY,
       substring_index(group_concat(PRICE order by PRICE desc), ',', 1) as MAX_PRICE,
       substring_index(group_concat(PRODUCT_NAME order by PRICE desc), ',' , 1) as PRODUCT_NAME
from FOOD_PRODUCT
where CATEGORY in ('과자', '국', '김치', '식용유')
group by CATEGORY
order by cast(MAX_PRICE as UNSIGNED) desc;


# 식품별로 가격기 제일 비싼 식품의 분류, 가겨그 이름을 조회하는 sql
# 식품분류가 과자 국 김치 식용유만 출력
# 식품 가격 기준 내림차순

# 1) 각 식품에서 가장 비싼 가격 정렬하기
# id까지 같이 그룹바이하면 아이디별 카테고리별 최고가가 나오니까 식용유에서도 최고가가 다양하게 나올 것!
with tmp as (
    select max(PRICE) as max_price, CATEGORY
    from FOOD_PRODUCT
    where CATEGORY in ('식용유', '과자', '국', '김치')
    group by CATEGORY
    
)

select P.CATEGORY, T.MAX_PRICE, P.PRODUCT_NAME
from tmp as T
inner join FOOD_PRODUCT as P on (P.CATEGORY = T.CATEGORY and P.PRICE = T.max_price)
order by max_price desc;