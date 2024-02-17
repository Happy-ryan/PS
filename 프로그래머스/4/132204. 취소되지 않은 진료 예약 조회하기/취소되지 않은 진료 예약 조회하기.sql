-- 코드를 입력하세요
# 2022년 4월 13일 기준
# 취소되지 않은 흉부외과(CS)
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
# 진료예약일시 기준 오름차순
with cs_docter as (
    select DR_NAME, MCDP_CD, DR_ID	
    from DOCTOR
    where MCDP_CD = 'CS'
), temp as (
    select A.APNT_NO, P.PT_NAME, P.PT_NO,  A.MCDP_CD, C.DR_NAME, A.APNT_YMD
    from APPOINTMENT A
    inner join PATIENT P on A.PT_NO = P.PT_NO
    inner join cs_docter C on C.DR_ID = A.MDDR_ID
    where A.APNT_YMD like '2022-04-13%'and A.APNT_CNCL_YN = 'N'
    order by A.APNT_YMD asc
)

select *
from temp;

# 43  바라  PT22000019  CS  니모  2022-04-13 15:30:00
