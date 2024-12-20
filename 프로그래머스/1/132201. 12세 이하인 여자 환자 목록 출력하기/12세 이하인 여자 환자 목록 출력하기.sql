-- 코드를 입력하세요
# NULL인 값이 조회되는 경우 NULL을 대체해서 출력해야할때 IFNULL(컬럼명, null인 경우 대체값)
# SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, "NONE") AS TLNO
# FROM PATIENT
# WHERE AGE <= 12 AND GEND_CD = "W"
# ORDER BY AGE DESC, PT_NAME ASC;


select pt_name, pt_no, gend_cd, age, ifnull(tlno, "NONE") as tlno
from patient
where age <= 12 and gend_cd = "W"
order by age desc, pt_name asc;

# 테이블 12세이하 여자환자 / 전화번호 없으면 none / 결과는 나이 내림차순, 이름 오름차순
select PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE') as TLNO
from PATIENT
where GEND_CD = 'W' and AGE <= 12
order by AGE desc, PT_NAME asc;


# 12세 이하 / 여자환자 / 전화번호 없으면 NONE 출력 / 나이 기준 내림차순 / 환자이름 오름차순
# ~ 필드 없으면 * 출력하라 -> isnull
select PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE')
from PATIENT
where GEND_CD = 'W' and AGE <= 12
order by AGE desc, PT_NAME asc;