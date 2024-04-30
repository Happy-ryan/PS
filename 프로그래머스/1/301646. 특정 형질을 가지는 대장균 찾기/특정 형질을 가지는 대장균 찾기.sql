-- 코드를 작성해주세요

select count(ID) as COUNT
from ECOLI_DATA
where (GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4) and (GENOTYPE & 2 = 0)