-- Ids share one namespace across principles, architectures, practices, backlog and session_log
-- (render.py's cross-link index is global, not scoped per table).
SELECT id, count(*) AS n, list(kind) AS tables
FROM (
  SELECT id, 'principles' AS kind FROM principles
  UNION ALL SELECT id, 'architectures' FROM architectures
  UNION ALL SELECT id, 'practices' FROM practices
  UNION ALL SELECT id, 'backlog' FROM backlog
  UNION ALL SELECT id, 'session_log' FROM session_log
)
GROUP BY id HAVING count(*) > 1;
