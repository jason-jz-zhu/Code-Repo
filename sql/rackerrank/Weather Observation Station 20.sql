/*
Enter your query here.
*/
SELECT ROUND(tmp.LAT_N, 4) AS median
FROM (
    SELECT s1.ID, s1.LAT_N, COUNT(s1.LAT_N) AS rank
    FROM STATION s1
    INNER JOIN STATION s2
    ON s1.LAT_N < s2.LAT_N OR (s1.LAT_N = s2.LAT_N AND s1.ID <= s2.ID)
    GROUP BY s1.ID, s1.LAT_N) AS tmp
WHERE tmp.rank = (SELECT (COUNT(*)+1) DIV 2 FROM STATION)
