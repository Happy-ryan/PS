-- 코드를 입력하세요
# SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
# FROM BOOK
# WHERE CATEGORY = "인문" AND YEAR(PUBLISHED_DATE) = "2021"
# ORDER BY PUBLISHED_DATE ASC;


select book_id, date_format(published_date, "%Y-%m-%d") as published_date
from book
where category = "인문" and year(published_date) = 2021
order by published_date asc;

-- 2021 출판 / 인문 / 도서id, 출판일 / 출판일 기준 오름차순
select BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK
where CATEGORY like '%인문%' and year(PUBLISHED_DATE) = 2021;

# 2021년 출판 / 인문 카테고리 / 아이디 출판일 기준 정렬
select BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
from BOOK
where year(PUBLISHED_DATE) = 2021 and CATEGORY like '인문';