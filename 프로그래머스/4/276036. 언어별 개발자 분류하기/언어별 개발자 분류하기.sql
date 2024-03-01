# -- 코드를 작성해주세요
# #  GRADE별 개발자의 정보를 조회
# # A : Front End 스킬과 Python 스킬을 함께 가지고 있는 개발자
# # B : C# 스킬을 가진 개발자
# # C : 그 외의 Front End 개발자
# # 존재하는 개발자의~
# # G / id 기준 오름차순

# # group_concat '1개의 String으로 인식!!' in 통하지 않는다 > Like로 판단함!
# # 1개를 나누고 싶으면 substring를 사용해야함. 총 개수가 필요해서 이 문제에서는 적절하지 않음.


# with temp as(
#     select D.ID, group_concat(S.NAME) as NAME,
#                  group_concat(S.CATEGORY) as CATEGORY
#     from DEVELOPERS D
#     inner join SKILLCODES S on D.SKILL_CODE & S.CODE = S.CODE
#     group by D.ID
# )

# select  case
#             when (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') then 'A'
#             when (T.NAME like '%C#%') then 'B'
#             when (T.CATEGORY like '%Front End%') then 'C'
#             else null
#         end as GRADE,
#         T.ID, D.EMAIL
# from temp T
# inner join DEVELOPERS D on T.ID = D.ID
# where   (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') or
#         (T.NAME like '%C#%') or
#         (T.CATEGORY like '%Front End%')
# order by GRADE asc, T.ID;



# A: front + python
# B: C#
# C: 그 외의 front 

with temp as (
    select  D.ID,
            group_concat(S.NAME) as NAME,
            group_concat(S.CATEGORY) as CATEGORY
    from DEVELOPERS D
    inner join SKILLCODES S on (D.SKILL_CODE & S.CODE) = S.CODE
    group by D.ID
)


select case
            when T.CATEGORY like '%Front End%' and T.NAME like '%Python%' then 'A'
            when T.NAME like '%C#%' then 'B'
            when T.CATEGORY like '%Front End%' then 'C'
        end as GRADE, 
        T.ID,
        D.EMAIL
from temp T
inner join DEVELOPERS D on T.ID = D.ID
where   (T.CATEGORY like '%Front End%' and T.NAME like '%Python%') or
        (T.NAME like '%C#%') or
        (T.CATEGORY like '%Front End%')
order by GRADE asc, T.ID asc;