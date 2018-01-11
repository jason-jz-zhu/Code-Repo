# Write your MySQL query statement below

SELECT question_id as survey_log
FROM (
    SELECT question_id,
        SUM(CASE
            WHEN action = 'answer' THEN 1
            ELSE 0
        END) AS num_ans,
        SUM(CASE
            WHEN action = 'show' THEN 1
            ELSE 0
        END) AS num_show
    FROM survey_log
    GROUP BY question_id) AS tmp
ORDER BY (tmp.num_ans / IF(tmp.num_show=0, 1, tmp.num_show)) DESC
LIMIT 1
