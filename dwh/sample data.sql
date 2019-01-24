SELECT * FROM infosec.accepted
order by rand()
limit 10;


SELECT * FROM infosec.accepted
where rand() < 0.02;


SELECT t.*
FROM table AS t
JOIN
(
  SELECT ROUND(RAND() * (SELECT MAX(id) FROM table )) AS id
) AS x
WHERE t.id >= x.id
LIMIT 1;
