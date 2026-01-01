-- 코드를 입력하세요
# SELECT U.USER_ID, SUM(B.PRICE) AS TOTAL_SALES
# FROM USED_GOODS_BOARD B
# INNER JOIN USED_GOODS_USER U ON B.WRITER_ID = U.USER_ID
# WHERE STATUS = 'DONE'
# GROUP BY U.USER_ID, U.NICKNAME
# HAVING SUM(B.PRICE) >= 700000
# ORDER BY TOTAL_SALES;

SELECT 
    B.WRITER_ID AS USER_ID, 
    U.NICKNAME, 
    SUM(B.PRICE) AS TOTAL_SALES
FROM 
    USED_GOODS_BOARD B, 
    USED_GOODS_USER U
WHERE 
    B.WRITER_ID = U.USER_ID
    AND B.STATUS = 'DONE'
GROUP BY 
    B.WRITER_ID, 
    U.NICKNAME
HAVING 
    SUM(B.PRICE) >= 700000
ORDER BY 
    TOTAL_SALES;
    
    
    
# 완료된 중고거래의 총 금액 70만원 이상
# 총 거래금액 기준 오름차순
with temp as (
    select WRITER_ID, sum(PRICE) as TOTAL_PRICE
    from USED_GOODS_BOARD
    where STATUS = 'DONE'
    group by WRITER_ID
    having TOTAL_PRICE >= 700000
)

select U.USER_ID, U.NICKNAME, T.TOTAL_PRICE
from temp T
inner join USED_GOODS_USER U on T.WRITER_ID = U.USER_ID
order by T.TOTAL_PRICE asc;

-- 완료된 중고거래 총 금액이 70만원 이상 회원ID, 닉네임, 총 거래금액
-- 총 거래금액 기준 오름차순

with done as (
    select B.WRITER_ID, sum(B.PRICE) as TOTAL_PRICE
    from USED_GOODS_BOARD as B
    left join USED_GOODS_USER as U on B.WRITER_ID = U.USER_ID
    where B.STATUS = 'DONE'
    group by B.WRITER_ID
    having TOTAL_PRICE >= 700000
    
)

select U.USER_ID, U.NICKNAME, D.TOTAL_PRICE
from done as D
left join USED_GOODS_USER as U on D.WRITER_ID = U.USER_ID
order by D.TOTAL_PRICE asc;


# 완료된 중고거래 / 유저별 !! 총 금액 70민원 이상 / 총 거래금액 기준 오름차순
with tmp as (
    select B.WRITER_ID, sum(PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD as B
    left join USED_GOODS_USER as U on B.WRITER_ID = U.USER_ID
    where B.STATUS = 'DONE'
    group by B.WRITER_ID
    having TOTAL_SALES >= 700000
    order by TOTAL_SALES asc
)

select U.USER_ID, U.NICKNAME, T.TOTAL_SALES
from tmp as T
inner join USED_GOODS_USER as U on T.WRITER_ID = U.USER_ID;




# 완료된 중고거래 & '총' (> group by > 매우 주의) 금액 70만원 이상 / 거래액 기준 오름차순

# 1) 완료된 중고거래 추출
with tmp as (
    select WRITER_ID, sum(PRICE) as 'TOTAL_SALES'
    from USED_GOODS_BOARD
    where STATUS = 'DONE'
    group by WRITER_ID
    having TOTAL_SALES >= 700000
)

select T.WRITER_ID, U.NICKNAME, T.TOTAL_SALES
from tmp as T
inner join USED_GOODS_USER as U on T.WRITER_ID = U.USER_ID
order by TOTAL_SALES asc;