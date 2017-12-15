/*
Enter your query here.
*/

SELECT X, Y
FROM
   (SELECT f1.X, f1.Y
    FROM Functions AS f1
    INNER JOIN Functions AS f2
    ON f1.X < f1.Y AND f1.X = f2.Y AND f1.Y = f2.X

    UNION

    SELECT X, Y
    FROM Functions
    WHERE X = Y
    GROUP BY X, Y
    HAVING COUNT(*) > 1) AS tmp
ORDER BY X
