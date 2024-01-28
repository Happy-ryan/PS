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