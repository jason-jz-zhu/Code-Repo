/*
Enter your query here.
*/
SELECT a.Start_Date, MIN(End_Date)
FROM (SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS a
INNER JOIN (SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) AS b
ON a.Start_Date < b.End_Date
GROUP BY a.Start_Date
ORDER BY DATEDIFF(MIN(End_Date), Start_Date) ASC, Start_Date ASC;
