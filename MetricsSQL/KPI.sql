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
select
  extract(year_month from last_login_time) as y_m,
  count(distinct user_id)
FROM login
GROUP BY y_m

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
      AND DATE(last_login_time) < current_date;

-- Just last 28 days
SELECT
  CONCAT(SUBDATE(current_date, 28), ' - ', SUBDATE(current_date, 1)) AS last_28_days,
  COUNT(DISTINCT user_id) AS last_28_days_au
FROM f.login
WHERE DATE(last_login_time) >= SUBDATE(current_date, 28)
      AND DATE(last_login_time) < current_date;

-- every day total Yesterday's DAU
SELECT
  DATE(today.last_login_time) AS d,
  COUNT(DISTINCT yesterday.user_id) AS yesterday_dau
FROM login AS today
LEFT JOIN login AS yesterday
ON subdate(DATE(today.last_login_time), 1) = DATE(yesterday.last_login_time)
GROUP BY DATE(today.last_login_time)

WITH dau AS (
  SELECT
    DATE(last_login_time) AS d,
    COUNT(DISTINCT user_id) AS cnt
  FROM login
  GROUP BY DATE(last_login_time)
)
SELECT
  today_dau.d,
  CASE WHEN yesterday_dau.d is null THEN 0 ELSE yesterday_dau.cnt END AS yesterday_dau
FROM dau AS today_dau
LEFT JOIN dau AS yesterday_dau
ON SUBDATE(today_dau.d, 1) = yesterday_dau.d;

-- every day total last 7 days DAU
SELECT
  date(today.last_login_time) as d,
    count(distinct past.user_id, date(past.last_login_time)) as past_7_cnt
FROM login AS today
LEFT JOIN login AS past
ON subdate(date(today.last_login_time), 7) <= date(past.last_login_time)
and date(today.last_login_time) > date(past.last_login_time)
GROUP by date(today.last_login_time)

-- new users
SELECT tmp.first_login_time, COUNT(tmp.user_id) AS new_users
FROM (
	SELECT user_id, MIN(last_login_time) AS first_login_time
	FROM f.login
	GROUP BY user_id) AS tmp
GROUP BY tmp.first_login_time;

-- retention/retained users (daily, weekly, monthly)
-- daily (1 day retention)
SELECT
  date(today.last_login_time) as today,
  COUNT(distinct future.user_id) as day1_retained_num,
  COUNT(distinct today.user_id) AS today_num
FROM login AS today
LEFT JOIN login AS future
ON future.user_id = today.user_id
AND subdate(date(today.last_login_time), -1) = date(future.last_login_time)
GROUP BY date(today.last_login_time)

-- monthly
with mau_detail as (
  select
    distinct extract(year_month from last_login_time) as y_m,
    user_id
  from login
)
select
  this_month.y_m,
  COUNT(distinct future_month.user_id) as month1_retained_num,
  COUNT(distinct this_month.user_id) as this_month_num
FROM mau_detail as this_month
LEFT JOIN mau_detail as future_month
ON this_month.user_id = future_month.user_id
and period_add(this_month.y_m, 1) = future_month.y_m
GROUP BY this_month.y_m

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
select
  date(today.last_login_time) as d,
  count(distinct today.user_id) as churn_num
FROM login AS today
LEFT JOIN login AS future
ON today.user_id = future.user_id
AND subdate(date(today.last_login_time), -1) = date(future.last_login_time)
WHERE future.user_id is null
GROUP BY date(today.last_login_time)


-- resurrected / reactive users
with first_activity as (
  select user_id, date(min(last_login_time)) as ts
  from login
  group by user_id
)
select date(today.last_login_time), count(distinct f.user_id)
from login as today
left join login as yesterday
on today.user_id = yesterday.user_id
and subdate(date(today.last_login_time), 1) = date(yesterday.last_login_time)
left join first_activity as f
on today.user_id = f.user_id
and f.ts != date(today.last_login_time)
where yesterday.user_id is null
group by date(today.last_login_time)
