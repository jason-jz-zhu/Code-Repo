/*
Enter your query here.
*/
SET @r1=0, @r2=0, @r3=0, @r4=0;
SELECT MIN(Doctor), MIN(Professor), MIN(SINGER), MIN(Actor)
FROM (
    SELECT
        CASE
            WHEN Occupation = 'Doctor' THEN @r1:=@r1 + 1
            WHEN Occupation = 'Professor' THEN @r2:=@r2 + 1
            WHEN Occupation = 'Singer' THEN @r3:=@r3 + 1
            WHEN Occupation = 'Actor' THEN @r4:=@r4 + 1
        END AS id,
        CASE WHEN Occupation = 'Doctor' THEN Name END AS 'Doctor',
        CASE WHEN Occupation = 'Professor' THEN Name END AS 'Professor',
        CASE WHEN Occupation = 'Singer' THEN Name END AS 'Singer',
        CASE WHEN Occupation = 'Actor' THEN Name END AS 'Actor'
    FROM OCCUPATIONS) AS tmp
GROUP BY tmp.id

SET @d=0, @a=0, @p=0, @s=0;
SELECT MIN(Doctor),MIN(Professor),MIN(SINGER),MIN(Actor)
FROM
(SELECT IF(OCCUPATION='Actor',NAME,NULL) AS Actor,
        IF(OCCUPATION='Doctor',NAME,NULL) AS Doctor,
        IF(OCCUPATION='Professor',NAME,NULL) AS Professor,
        IF(OCCUPATION='Singer',NAME,NULL) AS SINGER,
 CASE OCCUPATION
    WHEN 'Actor' THEN @a:=@a+1
    WHEN 'Doctor' THEN @d:=@d+1
    WHEN 'Professor' THEN @p:=@p+1
    WHEN 'Singer' THEN @s:=@s+1
 END
AS idn FROM OCCUPATIONS ORDER BY NAME )
AS temp GROUP BY temp.idn
