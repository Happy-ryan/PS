# -- 코드를 작성해주세요
# -- 사원별 성과금 보조 
# -- 사번기준 오름차순

# -- 1. 상하반기 점수 평균 구하기 테이블

# with grade as (
#     select EMP_NO, 
#         case
#             when avg(SCORE) >= 96 then 'S'
#             when avg(SCORE) >= 90 then 'A'
#             when avg(SCORE) >= 80 then 'B'
#             else 'C'
#         end as GRADE
#     from HR_GRADE
#     group by EMP_NO
# )

# select G.EMP_NO, E.EMP_NAME, G.GRADE, 
#         case
#             when G.GRADE = 'S' then E.SAL * 0.2
#             when G.GRADE = 'A' then E.SAL * 0.15
#             when G.GRADE = 'B' then E.SAL * 0.1
#             else E.SAL * 0
#         end as BONUS
# from grade as G
# left join HR_EMPLOYEES as E on G.EMP_NO = E.EMP_NO
# order by G.EMP_NO asc;


# 사원별 성과금 정보 조회
# 사번, 성명, 평가등급, 성과금 조회
# 사번 기준 오름차순

# 1) 각 사원의 점수에 따른 grade 부여
with tmp1 as (
    select G.EMP_NO,
        case 
            when avg(SCORE) >= 96 then 'S'
            when avg(SCORE) >= 90 then 'A'
            when avg(SCORE) >= 80 then 'B'
            else 'C'
        end as GRADE
    from HR_GRADE as G
    inner join HR_EMPLOYEES as H on G.EMP_NO = H.EMP_NO
    group by G.EMP_NO
)

select   T1.EMP_NO, E.EMP_NAME, T1.GRADE,
        case
            when T1.GRADE = 'S' then E.SAL * 0.2
            when T1.GRADE = 'A' then E.SAL * 0.15
            when T1.GRADE = 'B' then E.SAL * 0.1
            when T1.GRADE = 'C' then E.SAL * 0
        end as BONUS
from tmp1 as T1
inner join HR_EMPLOYEES as E on T1.EMP_NO = E.EMP_NO
order by T1.EMP_NO;