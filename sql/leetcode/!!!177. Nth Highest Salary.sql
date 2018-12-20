CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT (
          SELECT DISTINCT e1.Salary
          FROM Employee AS e1
          INNER JOIN Employee AS e2
          ON e1.Salary <= e2.Salary
          GROUP BY e1.Id, e1.Salary
          HAVING COUNT(DISTINCT e2.Salary) = N) AS getNthHighestSalary
  );
END

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END
