-- 코드를 작성해주세요
with temp as(
    select group_concat(S.NAME) as NAME, D.ID
    from DEVELOPERS D
    inner join SKILLCODES S on (D.SKILL_CODE & S.CODE) = S.CODE
    group by D.ID
)

select T.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from temp T
inner join DEVELOPERS D on T.ID = D.ID
where T.NAME like '%Python%' or T.NAME like '%C#%'
order by D.ID asc;