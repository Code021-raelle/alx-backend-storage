-- Task: Rank country origins of bands, ordered by the number
-- of (non-unique) fans
-- The result is ordered by `nb_fans` in descending order.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
