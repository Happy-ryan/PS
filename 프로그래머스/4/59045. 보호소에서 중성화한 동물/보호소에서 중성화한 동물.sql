-- 코드를 입력하세요
# 보호소 들어올 당시 중성화 x > 보호소 나갈 당시 중성화된 동물
# 동물의 id, 종, 이름
# id순으로 조회
with temp as (
    select ANIMAL_ID, ANIMAL_TYPE, NAME
    from ANIMAL_INS
    where SEX_UPON_INTAKE like 'Intact%'
)
select O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
from ANIMAL_OUTS O
inner join temp T on O.ANIMAL_ID = T.ANIMAL_ID	
where O.SEX_UPON_OUTCOME like 'Spayed%' or O.SEX_UPON_OUTCOME like 'Neutered%'
order by O.ANIMAL_ID;