-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, IFNULL(FREEZER_YN, 'N') AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE WAREHOUSE_NAME LIKE '창고_경기%'
ORDER BY WAREHOUSE_ID ASC;





select WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, ifnull(FREEZER_YN, 'N') AS FREEZER_YN
from FOOD_WAREHOUSE
where WAREHOUSE_NAME LIKE '%경기%'
order by WAREHOUSE_ID;











