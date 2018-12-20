-- Database Schema
-- purchases 2000 rows
-- id	int
-- user_id	int
-- price	real
-- refunded_at	text
-- created_at	text

-- gameplays 14000 rows
-- id	int
-- user_id	int
-- created_at	text
-- platform	text


-- Daily Revenue
select
  date(created_at) as d,
  round(sum(price), 2)
from purchases
group by d
order by d;

-- Daily Active Users
select
	date(created_at) as d,
  count(distinct user_id) as dau
from gameplays
group by d
order by d;

-- Daily Average Revenue Per Purchasing User
select
  date(created_at) as d,
  round(SUM(price) / count(distinct user_id), 2) as arppu
from purchases
where refunded_at is null
group by d
order by d;

-- 1 Day Retention
select
  date(g1.created_at) as dt,
  round(100 * count(distinct g2.user_id) /
    count(distinct g1.user_id)) as retention
from gameplays as g1
  left join gameplays as g2 on
    g1.user_id = g2.user_id
    and date(g1.created_at) = date(datetime(g2.created_at, '-1 day'))
group by 1
order by 1
limit 100;
