-- 코드를 입력하세요
# SELECT COUNT(USER_ID) AS USERS
# FROM USER_INFO
# WHERE JOINED LIKE "2021%" AND AGE BETWEEN 20 AND 29;


select count(USER_ID) as USERS
from USER_INFO
where date_format(JOINED, "%Y") = 2021 and age between 20 and 29;