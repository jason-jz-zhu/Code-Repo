# Write your MySQL query statement below
SELECT e1.Id, e1.Month, IFNULL(e1.salary, 0) + IFNULL(e2.salary, 0) + IFNULL(e3.salary, 0) AS Salary
FROM (SELECT Id, MAX(Month) AS Month FROM Employee GROUP BY Id HAVING COUNT(MONTH) > 1) AS maxMonth
LEFT JOIN Employee AS e1
ON maxMonth.Id = e1.Id AND maxMonth.Month > e1.Month
LEFT JOIN Employee AS e2
ON e1.id = e2.id AND e1.Month - 1 = e2.Month
LEFT JOIN Employee AS e3
ON e1.id = e3.id AND e1.Month - 2 = e3.Month
ORDER BY Id, Month DESC, Salary DESC
