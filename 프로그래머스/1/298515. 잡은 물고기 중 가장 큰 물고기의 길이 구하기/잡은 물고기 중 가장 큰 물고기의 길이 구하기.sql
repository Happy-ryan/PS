-- 코드를 작성해주세요

# select concat(LENGTH, 'cm') as MAX_LENGTH
# from FISH_INFO
# order by LENGTH desc
# limit 1;

select concat(max(LENGTH), 'cm') as MAX_LENGTH
from FISH_INFO;

