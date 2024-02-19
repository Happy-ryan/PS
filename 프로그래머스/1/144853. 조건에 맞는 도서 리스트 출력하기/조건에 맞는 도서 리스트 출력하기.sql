-- 코드를 입력하세요
# SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
# FROM BOOK
# WHERE CATEGORY = "인문" AND YEAR(PUBLISHED_DATE) = "2021"
# ORDER BY PUBLISHED_DATE ASC;


select book_id, date_format(published_date, "%Y-%m-%d") as published_date
from book
where category = "인문" and year(published_date) = 2021
order by published_date asc;