# Write your MySQL query statement below
SELECT t.Request_at AS Day,
        ROUND((SUM(CASE WHEN LOWER(Status) LIKE 'cancelled%' THEN 1.0 ELSE 0 END) / COUNT(t.id)), 2) AS 'Cancellation Rate'
FROM Trips AS t
INNER JOIN Users AS u
ON t.Client_Id = u.Users_Id
WHERE u.Banned = 'No' AND t.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.Request_ats
