-- 코드를 작성해주세요
-- 코드를 작성해주세요
-- percent_rank() 라는 윈도우함수 존재

# with tmp as (
#     select ID,
#         percent_rank() over (order by SIZE_OF_COLONY desc) as RN
#     from ECOLI_DATA
# )

# select ID,
#     case
#         when RN <= 0.25 then 'CRITICAL'
#         when RN <= 0.5 then 'HIGH'
#         when RN <= 0.75 then 'MEDIUM'
#         else 'LOW'
#     end as COLONY_NAME
# from tmp
# order by ID asc;

WITH tmp AS (
    SELECT ID,
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS NT
    FROM ECOLI_DATA
)

SELECT ID,
    CASE NT
        WHEN 1 THEN 'CRITICAL'
        WHEN 2 THEN 'HIGH'
        WHEN 3 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM tmp
ORDER BY ID ASC;