# Write your MySQL query statement below
SET @r1=0, @r2=0, @r3=0;
SELECT MIN(tmp.America) AS America, MIN(tmp.Asia) AS Asia, MIN(tmp.Europe) AS Europe
FROM (
    SELECT
        CASE
            WHEN continent = 'America' THEN @r1:=@r1 + 1
            WHEN continent = 'Asia' THEN @r2:=@r2 + 1
            WHEN continent = 'Europe' THEN @r3:=@r3 + 1
        END AS id,
        CASE WHEN continent = 'America' THEN name END AS 'America',
        CASE WHEN continent = 'Asia' THEN name END AS 'Asia',
        CASE WHEN continent = 'Europe' THEN name END AS 'Europe'
    FROM student
    ORDER BY name) AS tmp
GROUP BY tmp.id
