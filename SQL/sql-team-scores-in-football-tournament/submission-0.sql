
-- 3 points for a win (scoring more goals than the opponent)
-- 1 point for a draw (scoring the same number of goals)
-- 0 points for a loss (scoring fewer goals)

SELECT team_id, team_name, 
COALESCE(SUM(CASE
    WHEN team_id = host_team AND host_goals > guest_goals THEN 3
    WHEN team_id = guest_team AND guest_goals > host_goals THEN 3
    WHEN guest_goals = host_goals THEN 1
    ELSE 0
END ), 0) AS  num_points
FROM Teams as t 
LEFT JOIN Matches m
    ON t.team_id = m.host_team or t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, t.team_id