-- 코드를 입력하세요
SELECT USER_ID,	PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
# 재구매 주의! 1초과해야함
HAVING COUNT(PRODUCT_ID) > 1
ORDER BY USER_ID ASC, PRODUCT_ID DESC;