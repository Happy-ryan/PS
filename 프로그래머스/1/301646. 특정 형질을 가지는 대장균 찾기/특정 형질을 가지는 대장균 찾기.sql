-- 코드를 작성해주세요
-- substring(1010, -1, 1) = 0
-- substring(1010, -2, 1) = 1
-- substring(1010, -3, 1) = 0
-- substring(1010, -4, 1) = 1
    
select count(*) as COUNT
from ECOLI_DATA
where   (substring(conv(GENOTYPE, 10, 2), -1, 1) = 1 or
        substring(conv(GENOTYPE, 10, 2), -3, 1) = 1) and
        (substring(conv(GENOTYPE, 10, 2), -2, 1) = 0)