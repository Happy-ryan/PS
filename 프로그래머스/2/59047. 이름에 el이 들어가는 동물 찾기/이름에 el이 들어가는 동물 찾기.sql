-- 코드를 입력하세요
# select ANIMAL_ID, NAME
# from ANIMAL_INS
# where (NAME like "%el%" or NAME like "%El%" or NAME like "%EL%" or NAME like "%eL%") and
#     ANIMAL_TYPE like "Dog"
# order by NAME asc;

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE lower(NAME) LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC;








# 동물 이름 중 EL 들어가는 개의 아이디와 이름 조회
# 대문자 소문자로 이름이 나뉘어져있으니 대문자든 소문자든 하나로 변경해야함.
# upper / lower
# 이름순 조회
select ANIMAL_ID, NAME
from ANIMAL_INS
where ANIMAL_TYPE like 'Dog' and upper(NAME) like '%EL%'
order by NAME asc;

