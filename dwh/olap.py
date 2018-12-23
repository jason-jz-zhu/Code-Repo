# Drill-down
# 将汇总数据拆分到更细节的数据





# Roll-up
# 从细粒度数据向高层的聚合


# SQL
SELECT month, SUM(amount) FROM test

# coding
hashmap



# Slice
# 选择维中特定的值进行分析

# SQL
SELECT * FROM test WHERE city = 'shanghai'

# coding
if statement




# Dice
# 选择维中特定区间的数据

# SQL
SELECT * FROM test WHERE day between '2018' and '2019'

# coding
if statement



# Pivot
# 维的位置的互换

# SQL
SELECT conference,
       SUM(players) AS total_players,
       SUM(CASE WHEN year = 'FR' THEN players ELSE NULL END) AS fr,
       SUM(CASE WHEN year = 'SO' THEN players ELSE NULL END) AS so,
       SUM(CASE WHEN year = 'JR' THEN players ELSE NULL END) AS jr,
       SUM(CASE WHEN year = 'SR' THEN players ELSE NULL END) AS sr
  FROM test
 GROUP BY conference
 ORDER BY total_players DESC

SELECT a.m,
	   b.year,
	   case
		when year = 2000 then `year_2000`
		when year = 2001 then `year_2001`
        else null
	   end as amount
FROM f.worldwide_earthquakes as a
CROSS JOIN (select 2000  as year union select 2001) as b



# coding
