-- 코드를 입력하세요
# SELECT A.FLAVOR AS FLAVOR
# FROM FIRST_HALF A
# INNER JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
# WHERE B.INGREDIENT_TYPE = "fruit_based" AND A.TOTAL_ORDER > 3000
# ORDER BY A.TOTAL_ORDER DESC;


# select i.FLAVOR as FLAVOR
# from FIRST_HALF f
# -- 두 테이블의 공통 col만 존재함!
# inner join ICECREAM_INFO i on f.FLAVOR = i.FLAVOR
# where f.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE = "fruit_based"
# order by f.TOTAL_ORDER desc;


# 총 주문량 >= 3000 & 주성분 = 과일 
# 총 주문량으로 정렬
select H.FLAVOR
from FIRST_HALF AS H
left join ICECREAM_INFO AS I ON H.FLAVOR = I.FLAVOR
where H.TOTAL_ORDER >= 3000 and I.INGREDIENT_TYPE = 'fruit_based';














