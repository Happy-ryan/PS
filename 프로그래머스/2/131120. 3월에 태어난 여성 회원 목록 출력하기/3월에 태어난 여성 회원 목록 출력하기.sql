-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,'%Y-%m-%d')AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = "W" 
    AND MONTH(DATE_OF_BIRTH) = 3 
    AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER = "W" 
    AND DATE_OF_BIRTH LIKE "%-03-%"
    AND TLNO IS NOT NULL
ORDER BY MEMBER_ID ASC;


select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
from MEMBER_PROFILE
where TLNO is not null and GENDER = "W" and month(DATE_OF_BIRTH) = "03"
order by MEMBER_ID asc;

# 생일 3월 / 여성 / 전화번호 null이면 제외 / id기준 오름차순
select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' and TLNO is not null and month(DATE_OF_BIRTH) = 3
order by MEMBER_ID asc;


# 생일 3월 / 여성회원 / ID, 이름, 성별, 생년월일
# 월 체크하는 방법 - month(Date 타입 필드)
# 출력형식 - date_format(컬럼명, '%Y-%m-%d')
# 전화번호 NULL 제외 - is not null / is null
# 회원ID 기준 오름차순 - order by asc, orde by desc
select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH,  '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' and TLNO is not null and month(DATE_OF_BIRTH) = 3
order by MEMBER_ID asc;

select MEMBER_ID, MEMBER_NAME, GENDER, date_format(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where TLNO is not null and DATE_OF_BIRTH like '%-03-%' and GENDER = 'W'
order by MEMBER_ID asc;