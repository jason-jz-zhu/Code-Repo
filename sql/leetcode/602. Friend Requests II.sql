# Write your MySQL query statement below
SELECT tmp.id, SUM(cnt) AS num
FROM
    (SELECT requester_id AS id, COUNT(*) AS cnt
     FROM request_accepted
     GROUP BY requester_id
     UNION ALL
     SELECT accepter_id AS id, COUNT(*) AS cnt
     FROM request_accepted
     GROUP BY accepter_id) AS tmp
GROUP BY tmp.id
ORDER BY num DESC
LIMIT 1


# Write your MySQL query statement below
SELECT tmp.id, COUNT(*) AS num
FROM
    (SELECT requester_id AS id
    FROM request_accepted
    UNION ALL
    SELECT accepter_id AS id
    FROM request_accepted) AS tmp
GROUP BY tmp.id
ORDER BY COUNT(*) DESC
LIMIT 1
