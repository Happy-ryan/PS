-- 코드를 입력하세요
# 소수점버림 FLOOR 10000단위라서 모듈러 연산 활용 
# 표현은 10000단위이므로 10000를 곱해야함.
# 개수 세는 집계함수
SELECT FLOOR(PRICE / 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC;

# 만원단위의 가격대별로 상품의 개수 출력
# 버림!
select floor(PRICE / 10000) * 10000 as PRICE_GROUP, COUNT(*) AS PRODUCTS
from PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP ASC;