# select sum(PRICE) as TOTAL_PRICE
# from ITEM_INFO
# where RARITY = 'LEGEND';

# 희귀도가 legend / 아이템들의 가격의 총합
select sum(PRICE) as TOTAL_PRICE
from ITEM_INFO
where RARITY = 'LEGEND';