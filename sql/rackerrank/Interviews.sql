SELECT
    con.`contest_id`,
    con.`hacker_id`,
    con.`name`,
    COALESCE(SUM(SG.`total_submissions`), 0) AS `total_submissions`,
    COALESCE(SUM(SG.`total_accepted_submissions`), 0) AS `total_accepted_submissions`,
    COALESCE(SUM(VG.`total_views`), 0) AS `total_views`,
    COALESCE(SUM(VG.`total_unique_views`), 0) AS `total_unique_views`
FROM `Contests` con
    INNER JOIN `Colleges` col ON con.`contest_id` = col.`contest_id`
    INNER JOIN `Challenges` cha ON col.`college_id` = cha.`college_id`
    LEFT JOIN (
      SELECT
        V.`challenge_id`,
        SUM(V.`total_views`) AS `total_views`,
        SUM(V.`total_unique_views`) AS `total_unique_views`
      FROM `View_Stats` V
      GROUP BY V.`challenge_id`
    ) VG ON cha.`challenge_id` = VG.`challenge_id`
    LEFT JOIN (
      SELECT
        S.`challenge_id`,
        SUM(S.`total_submissions`) AS `total_submissions`,
        SUM(S.`total_accepted_submissions`) AS `total_accepted_submissions`
      FROM `Submission_Stats` S
      GROUP BY S.`challenge_id`
    ) SG ON cha.`challenge_id` = SG.`challenge_id`
GROUP BY
    con.`contest_id`, con.`hacker_id`, con.`name`
HAVING
    `total_submissions` +
    `total_accepted_submissions` +
    `total_views` +
    `total_unique_views` <> 0
ORDER BY
    con.`contest_id`
    
