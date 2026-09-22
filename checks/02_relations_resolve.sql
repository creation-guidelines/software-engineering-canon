-- Both ends of every relation must be an existing id (concept, backlog item, or log entry).
WITH c AS (
  SELECT id FROM principles UNION ALL SELECT id FROM architectures
  UNION ALL SELECT id FROM practices UNION ALL SELECT id FROM backlog
  UNION ALL SELECT id FROM session_log
)
SELECT 'from_id' AS end_, from_id AS missing_id FROM relations WHERE from_id NOT IN (SELECT id FROM c)
UNION ALL
SELECT 'to_id', to_id FROM relations WHERE to_id NOT IN (SELECT id FROM c);
