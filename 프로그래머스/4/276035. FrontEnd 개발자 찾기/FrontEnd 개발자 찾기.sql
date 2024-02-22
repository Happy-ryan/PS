-- 코드를 작성해주세요
# frontend 스킬을 가진 개발자의 정보를 조회

select distinct D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
from SKILLCODES S
inner join DEVELOPERS D on (D.SKILL_CODE & S.CODE) = S.CODE
where S.CATEGORY = 'Front End'
order by D.ID asc;