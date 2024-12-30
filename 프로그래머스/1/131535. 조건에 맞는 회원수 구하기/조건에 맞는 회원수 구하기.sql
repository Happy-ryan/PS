-- 코드를 입력하세요
# SELECT COUNT(USER_ID) AS USERS
# FROM USER_INFO
# WHERE JOINED LIKE "2021%" AND AGE BETWEEN 20 AND 29;


# select count(USER_ID) as USERS
# from USER_INFO
# where date_format(JOINED, "%Y") = 2021 and age between 20 and 29;

# A 이상 B 이하 -> filed between A and B;
# 행의 수 -> count
select count(USER_ID) as USERS
from USER_INFO
where year(JOINED) = "2021" and age between 20 and 29;


select count(*) as USERS
from USER_INFO
where year(JOINED) = 2021 and AGE between 20 and 29;

# 2021년에 가입 / 20세이상 29세 이하 / 몇 명
select count(USER_ID) as USERS
from USER_INFO
where year(JOINED) = 2021 and age between 20 and 29;