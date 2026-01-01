-- 코드를 입력하세요
select ANIMAL_ID, NAME,
    if(SEX_UPON_INTAKE like 'Neutered%' or SEX_UPON_INTAKE like 'Spayed%', 'O', 'X') as '중성화'
from ANIMAL_INS;


select ANIMAL_ID, NAME,
        if(SEX_UPON_INTAKE like 'Neutered%' or SEX_UPON_INTAKE like 'Spayed%',
            'O', 'X') as 중성화
            
from ANIMAL_INS;












# 중성화 판단 - 중성화 되어있다면 O / 아니면 X
# 아이디 오름차순
select ANIMAL_ID, NAME,
        if(SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%', 'O', 'X') as 중성화
from ANIMAL_INS
order by ANIMAL_ID asc;

select ANIMAL_ID, NAME,
case
    when SEX_UPON_INTAKE like '%Neutered%' or SEX_UPON_INTAKE like '%Spayed%' then 'O'
    else 'X'
end as '중성화'
from ANIMAL_INS
order by ANIMAL_ID asc;