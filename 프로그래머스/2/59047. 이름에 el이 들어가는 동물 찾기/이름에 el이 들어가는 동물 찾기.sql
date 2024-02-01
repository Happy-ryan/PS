-- 코드를 입력하세요
select ANIMAL_ID, NAME
from ANIMAL_INS
where (NAME like "%el%" or NAME like "%El%" or NAME like "%EL%" or NAME like "%eL%") and
    ANIMAL_TYPE like "Dog"
order by NAME asc;