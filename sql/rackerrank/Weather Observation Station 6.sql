SELECT DISTINCT CITY
FROM STATION
WHERE CITY RLIKE '^(a|e|i|o|u).*'
-- WHERE CITY RLIKE '^[aeiou].*'
