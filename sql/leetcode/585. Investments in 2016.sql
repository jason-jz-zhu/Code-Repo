# Write your MySQL query statement below
SELECT ROUND(SUM(DISTINCT i1.TIV_2016), 2) AS TIV_2016
FROM insurance AS i1
CROSS JOIN insurance AS i2
WHERE i1.PID != i2.PID AND i1.TIV_2015 = i2.TIV_2015
AND NOT EXISTS
    (SELECT *
    FROM insurance i3
    WHERE i1.lat = i3.lat AND i1.lon = i3.lon AND i1.pid != i3.pid)


# Write your MySQL query statement below
SELECT ROUND(SUM(DISTINCT i1.TIV_2016), 2) AS TIV_2016
FROM insurance AS i1
CROSS JOIN insurance AS i2
WHERE i1.PID != i2.PID AND i1.TIV_2015 = i2.TIV_2015
AND (i1.LAT,i1.LON) NOT IN (
    SELECT LAT, LON FROM insurance GROUP BY LAT, LON HAVING COUNT(*) > 1
)
