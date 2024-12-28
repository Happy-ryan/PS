-- 코드를 입력하세요
# 동물보호소에 '들어온'
# 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty
# 아이디, 이름, 성별, 중성화 여부
# 아이디순 조회
select ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by ANIMAL_ID;

select ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by ANIMAL_ID asc;