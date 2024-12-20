-- 코드를 작성해주세요

# and 와 or 조건이 존재한다는 것!!

# select ID, EMAIL, FIRST_NAME, LAST_NAME
# from DEVELOPER_INFOS
# where SKILL_1 = 'Python' or 
#     SKILL_2 = 'Python' or
#     SKILL_3 = 'Python'
# order by ID asc;

select ID, EMAIL, FIRST_NAME, LAST_NAME
from DEVELOPER_INFOS
where SKILL_1 IN ('Python') or 
      SKILL_2 IN ('Python') or 
      SKILL_3 IN ('Python') 
order by ID asc;