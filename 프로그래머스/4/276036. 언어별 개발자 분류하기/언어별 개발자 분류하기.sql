# # -- 코드를 작성해주세요
# # #  GRADE별 개발자의 정보를 조회
# # # A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
# # # B : C# 스킬을 가진 개발자
# # # C : 그 외의 Front End 개발자
# # # 존재하는 개발자의~
# # # G / id 기준 오름차순

# # # group_concat '1개의 String으로 인식!!' in 통하지 않는다 > Like로 판단함!
# # # 1개를 나누고 싶으면 substring를 사용해야함. 총 개수가 필요해서 이 문제에서는 적절하지 않음.

# # with temp as(
# #     select D.ID, group_concat(S.NAME) as NAME,
# #                  group_concat(S.CATEGORY) as CATEGORY
# #     from DEVELOPERS D
# #     inner join SKILLCODES S on D.SKILL_CODE & S.CODE = S.CODE
# #     group by D.ID
# # )

# # select  case
# #             when (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') then 'A'
# #             when (T.NAME like '%C#%') then 'B'
# #             when (T.CATEGORY like '%Front End%') then 'C'
# #             else null
# #         end as GRADE,
# #         T.ID, D.EMAIL
# # from temp T
# # inner join DEVELOPERS D on T.ID = D.ID
# # where   (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') or
# #         (T.NAME like '%C#%') or
# #         (T.CATEGORY like '%Front End%')
# # order by GRADE asc, T.ID;



# # A: front + python
# # B: C#
# # C: 그 외의 front 

# /*
# with temp as (
#     select  D.ID,
#             group_concat(S.NAME) as NAME,
#             group_concat(S.CATEGORY) as CATEGORY
#     from DEVELOPERS D
#     inner join SKILLCODES S on (D.SKILL_CODE & S.CODE) = S.CODE
#     group by D.ID
# )


# select case
#             when T.CATEGORY like '%Front End%' and T.NAME like '%Python%' then 'A'
#             when T.NAME like '%C#%' then 'B'
#             when T.CATEGORY like '%Front End%' then 'C'
#         end as GRADE, 
#         T.ID,
#         D.EMAIL
# from temp T
# inner join DEVELOPERS D on T.ID = D.ID
# # group by에서 정의한 것 이외의 컬럼 쓸 수 없다!
# # where 절에서는 alias 사용 불가다!
# where   (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') or
#         (T.NAME like '%C#%') or
#         (T.CATEGORY like '%Front End%')
# order by GRADE asc, T.ID asc;

# */

# -- GRADE별 개발자 정보 조회
# -- A에 B가 포함되는가(이진법) = > A & B = B
# -- 1. 각 디벨로퍼의 SKILL_CODE > GRADE로 변경!
# -- 테이블 group by D165 - 256 , 128, 16 > group by 1개만 남음... > 3개 필요해!
# with grade as (
#     select  D.ID,
#             group_concat(S.NAME) as SKILL,
#             group_concat(S.CATEGORY) as CATEGORY
#     from DEVELOPERS as D
#     inner join SKILLCODES as S on (D.SKILL_CODE & S.CODE = S.CODE)
#     group by D.ID
# )

# select  case
#             when (G.CATEGORY like '%Front End%') and (G.SKILL like '%Python%') then 'A'
#             when (G.SKILL like '%C#%') then 'B'
#             when (G.CATEGORY like '%Front End%') then 'C'
#         end as GRADE,
#         G.ID, 
#         D.EMAIL          
# from grade as G
# inner join DEVELOPERS as D on G.ID = D.ID
# where   ((G.CATEGORY like '%Front End%') and (G.SKILL like '%Python%')) or
#         (G.SKILL like '%C#%') or
#         (G.CATEGORY like '%Front End%')
# order by GRADE asc, G.ID asc;

# case-when문 공부

# 1) 각 개발자가 가지고 있는 스킬 추출
with tmp1 as (
    select D.ID,
           group_concat(S.NAME) as NAME
    from DEVELOPERS as D
    inner join SKILLCODES as S on (D.SKILL_CODE & S.CODE = S.CODE)
    group by D.ID
)

select case
        when T1.NAME like '%Python%' and (T1.NAME like '%JavaScript%' or T1.NAME like '%React%' or T1.NAME like '%Vue%') then 'A'
        when T1.NAME like '%C#%' then 'B'
        when (T1.NAME like '%JavaScript%' or T1.NAME like '%React%' or T1.NAME like '%Vue%') then 'C'
     end as GRADE, D.ID, D.EMAIL
from tmp1 as T1
inner join DEVELOPERS as D on T1.ID = D.ID
where (T1.NAME like '%Python%' and (T1.NAME like '%JavaScript%' or T1.NAME like '%React%' or T1.NAME like '%Vue%')) or
    (T1.NAME like '%C#%') or (T1.NAME like '%JavaScript%' or T1.NAME like '%React%' or T1.NAME like '%Vue%')
order by GRADE asc, D.ID asc
;
