-- 코드를 입력하세요
# 모든 레코드 동물id, 이름, 들어온 날짜
# id순으로
# datetime > date만!
select ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') as 날짜
from ANIMAL_INS
order by ANIMAL_ID asc;