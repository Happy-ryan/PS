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

# 2022년 4월 13일 취소되지 않는 흉부외과 진료예약
# 예약번호, 환지이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
# 진료예약일시 오름차순

with temp as (
    select APNT_NO, PT_NO, MCDP_CD, MDDR_ID, APNT_YMD
    from APPOINTMENT
    where (year(APNT_YMD) = 2022 and month(APNT_YMD) = 4 and day(APNT_YMD) = 13) and
        APNT_CNCL_YN = 'N' and
        MCDP_CD = 'CS'
)

select T.APNT_NO, P.PT_NAME, T.PT_NO, T.MCDP_CD, D.DR_NAME, T.APNT_YMD
from temp T
inner join PATIENT P on T.PT_NO = P.PT_NO
inner join DOCTOR D on T.MDDR_ID = D.DR_ID
order by  T.APNT_YMD asc;



# 2022년 4월 13일에 취소되지 않은 흉부외과(CS) 진료 예약 내역 조회
# 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
# 진료예약일시 기준 오름차순 정렬

select A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
from APPOINTMENT as A
inner join DOCTOR as D on A.MDDR_ID = D.DR_ID
inner join PATIENT as P on A.PT_NO = P.PT_NO
where timestampdiff(day, '2022-04-13', A.APNT_YMD) = 0 and
      D.MCDP_CD like 'CS' and
      A.APNT_CNCL_YN = 'N'
order by A.APNT_YMD	asc;


# 2022년 4월 13일 취소되지 않는 흉부외과(CS) 진료 예약 내역 조회
# 진료예약일시 기준 오름차순

with tmp as (
    select  A.APNT_NO,
            P.PT_NAME,
            P.PT_NO,
            A.MCDP_CD,
            D.DR_NAME,
            A.APNT_YMD
    from APPOINTMENT as A
    inner join DOCTOR as D on A.MDDR_ID = D.DR_ID
    inner join PATIENT as P on A.PT_NO = P.PT_NO
    where A.MCDP_CD = 'CS' and A.APNT_CNCL_YN = 'N' and
        year(A.APNT_YMD) = 2022 and month(A.APNT_YMD) = 4 and day(A.APNT_YMD) = 13
)

select *
from tmp
order by APNT_YMD asc;

# 2022 4 13 취소되지 않은 흉부외과(CS) 진료예약 조회
# 예약일시 기준 오름차순
select      A.APNT_NO,
            P.PT_NAME,
            P.PT_NO,
            A.MCDP_CD,
            D.DR_NAME,
            A.APNT_YMD
from APPOINTMENT as A
left join PATIENT as P on A.PT_NO = P.PT_NO
left join DOCTOR as D on A.MDDR_ID = D.DR_ID
where A.APNT_YMD like '2022-04-13%' and D.MCDP_CD = 'CS' and A.APNT_CNCL_YN = 'N'
order by A.APNT_YMD asc;