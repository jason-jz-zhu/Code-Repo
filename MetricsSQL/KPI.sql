-- DAU
SELECT
  DATE(last_login_time),
  COUNT(DISTINCT user_id)
FROM f.login
GROUP BY DATE(last_login_time);

-- WAU
SELECT
  YEAR(last_login_time) AS year,
  WEEK(last_login_time) AS week,
  COUNT(DISTINCT user_id) AS wau
FROM f.login
GROUP BY YEAR(last_login_time), WEEK(last_login_time);

-- MAU
SELECT
  YEAR(last_login_time) AS year,
  MONTH(last_login_time) AS month,
  COUNT(DISTINCT user_id) AS mau
FROM f.login
GROUP BY YEAR(last_login_time), MONTH(last_login_time);

-- Just Yesterday's DAU
SELECT
  SUBDATE(current_date, 1) AS yesterday,
  COUNT(DISTINCT user_id) AS dau
FROM f.login
WHERE DATE(last_login_time) = SUBDATE(current_date, 1);

-- Just last 7 days
SELECT
  CONCAT(SUBDATE(current_date, 7), ' - ', SUBDATE(current_date, 1)) AS last_7_days,
  COUNT(DISTINCT user_id) AS last_7_days_au
FROM f.login
WHERE DATE(last_login_time) >= SUBDATE(current_date, 7)
      AND DATE(last_login_time) <= SUBDATE(current_date, 1);

-- Just last 28 days
SELECT
  CONCAT(SUBDATE(current_date, 28), ' - ', SUBDATE(current_date, 1)) AS last_28_days,
  COUNT(DISTINCT user_id) AS last_28_days_au
FROM f.login
WHERE DATE(last_login_time) >= SUBDATE(current_date, 28)
      AND DATE(last_login_time) <= SUBDATE(current_date, 1);

-- every day total Yesterday's DAU
SELECT
  dau1.d AS day,
  CASE WHEN dau2.dau IS NULL THEN 0 ELSE dau2.dau END AS yesterday_dau
FROM
  (SELECT
      DATE(last_login_time) AS d,
      COUNT(DISTINCT user_id) AS dau
    FROM f.login
    GROUP BY DATE(last_login_time)) as dau1
LEFT JOIN (SELECT
    DATE(last_login_time) AS d,
    COUNT(DISTINCT user_id) AS dau
  FROM f.login
  GROUP BY DATE(last_login_time)) AS dau2
ON SUBDATE(dau1.d, 1) = dau2.d

-- every day total last 7 days DAU
SELECT dau1.d AS last_7_days, CASE WHEN SUM(dau2.dau) IS NULL THEN 0 ELSE SUM(dau2.dau) END AS last_7_days_au
FROM
(SELECT
  DATE(last_login_time) AS d,
  COUNT(DISTINCT user_id) AS dau
FROM f.login
GROUP BY DATE(last_login_time)) as dau1
LEFT JOIN (SELECT
  DATE(last_login_time) AS d,
  COUNT(DISTINCT user_id) AS dau
FROM f.login
GROUP BY DATE(last_login_time)) AS dau2
ON subdate(dau1.d, 1) >= dau2.d AND subdate(dau1.d, 7) <= dau2.d
GROUP BY dau1.d

-- new users
SELECT tmp.first_login_time, COUNT(tmp.user_id) AS new_users
FROM (
	SELECT user_id, MIN(last_login_time) AS first_login_time
	FROM f.login
	GROUP BY user_id) AS tmp
GROUP BY tmp.first_login_time;

-- retention/retained users (daily, weekly, monthly)
-- daily
SELECT
  DATE(l1.last_login_time),
  COUNT(DISTINCT l2.user_id)
FROM login AS l1
LEFT JOIN login AS l2
ON SUBDATE(DATE(l1.last_login_time), 1) = DATE(l2.last_login_time) AND l1.user_id = l2.user_id
GROUP BY DATE(l1.last_login_time);

-- monthly
SELECT
  this_month.ym AS 'year_month',
  COUNT(last_month.user_id) AS retention_number
FROM (SELECT DISTINCT CONCAT(YEAR(last_login_time), MONTH(last_login_time)) AS ym, user_id FROM login) AS this_month
LEFT JOIN (SELECT DISTINCT CONCAT(YEAR(last_login_time), MONTH(last_login_time)) AS ym, user_id FROM login) AS last_month
ON this_month.ym = last_month.ym + 1 AND this_month.user_id = last_month.user_id
GROUP BY this_month.ym

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

-- Day 7 retention
WITH new_user_activity AS (
	SELECT a.*
    FROM activity AS a
    INNER JOIN users AS u
    ON date(a.ts) = date(u.date) AND a.user_id = u.id
), new_user_cnt_by_date AS (
	SELECT ts, COUNT(DISTINCT user_id) AS cnt
    FROM new_user_activity
    GROUP BY ts
)
SELECT
	tmp.date,
    CONCAT('DAY ', period) AS period,
    new_users,
    retained_users,
    retention
FROM (
	SELECT
		DATE(first_activity.ts) AS date,
		DATEDIFF(future_activity.ts, first_activity.ts) AS period,
		MAX(cnt) AS new_users,
		COUNT(DISTINCT future_activity.user_id) AS retained_users,
		COUNT(DISTINCT future_activity.user_id) / MAX(cnt) AS retention
	FROM new_user_activity AS first_activity
	LEFT JOIN activity AS future_activity
	ON first_activity.user_id = future_activity.user_id
	AND DATE(first_activity.ts) < DATE(future_activity.ts)
	AND SUBDATE(DATE(first_activity.ts), -7) >= DATE(future_activity.ts)
	LEFT JOIN new_user_cnt_by_date AS cnt
	ON DATE(first_activity.ts) = DATE(cnt.ts)
	GROUP BY date, period) AS tmp
WHERE period IS NOT null
ORDER BY date, period

-- churn users
SELECT
  SUBDATE(DATE(yesterday.last_login_time), -1) AS day,
  COUNT(DISTINCT yesterday.user_id) AS churn_number
FROM login AS yesterday
LEFT JOIN login AS today
ON SUBDATE(DATE(today.last_login_time), 1) = DATE(yesterday.last_login_time) AND today.user_id = yesterday.user_id
WHERE today.user_id IS NULL
GROUP BY DATE(yesterday.last_login_time);

-- resurrected / reactive users
with
monthly_activity as (
  select distinct
    date_trunc('month', created_at) as month,
    user_id
  from events
),
first_activity as (
  select user_id, date(min(created_at)) as month
  from events
  group by 1
)
select
  this_month.month,
  count(distinct user_id)
from monthly_activity this_month
left join monthly_activity last_month
  on this_month.user_id = last_month.user_id
  and this_month.month = add_months(last_month.month,1)
join first_activity
  on this_month.user_id = first_activity.user_id
  and first_activity.month != this_month.month
where last_month.user_id is null
group by 1

-- Percent Change
with monthly_active_users as (
 select
   date_trunc('month', created_at) as month,
   count (distinct user_id) as mau
 from events
 group by 1
)
select
 this_month.month,
 [(this_month.mau - last_month.mau)*1.0/last_month.mau:%] as pct_change
from monthly_active_users this_month
join monthly_active_users last_month
 on this_month.month = add_months(last_month.month,1)


-- Daily Revenue
select
  date(created_at) as d,
  round(sum(price), 2)
from purchases
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
